from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
# from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


from .forms import ProfileForm
from ..comments.models import Comment


# class AddUserCreateView(SuccessMessageMixin, CreateView):
class AddUserCreateView(CreateView):
    model = User
    template_name = 'accounts/add_user.html'
    fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password',
    ]
    success_url = reverse_lazy('accounts:add_user')
    # success_message = _('Create an account successfully. Login enabled.')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.set_password(f.password)
        f.save()
        messages.success(self.request, _('Create an account successfully. Login enabled.'))
        return redirect(self.success_url)

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         f = form.save()
    #         f.set_password(f.password)
    #     return self.form_valid(form)


class UserLogin(LoginView):
    template_name = 'accounts/login_user.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user.is_authenticated:
            login(request, user)
            messages.success(request, _('Login sucessfully!'))
            return redirect('accounts:dashboard')
        messages.error(request, _('Error, invalid login!'))
        return redirect('accounts:login_user')


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context = {
        'comments_unread': Comment.objects.filter(read=False, user=request.user).order_by('-id'),
        'comments_read': Comment.objects.filter(read=True, user=request.user).order_by('-id')
    }
    return render(request, template_name, context)


@login_required
def create_profile(request):
    template_name = 'accounts/profile.html'
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, _('Profile successfully saved.'))
            return redirect('accounts:dashboard')

    context = {
        'form': ProfileForm()
    }
    return render(request, template_name, context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')
