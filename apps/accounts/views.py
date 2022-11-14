from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
# from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


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
        if user:
            login(request, user)
            messages.success(request, _('Login sucessfully!'))
            return redirect('accounts:login_user')
        messages.error(request, _('Error, invalid login!'))
        return redirect('accounts:login_user')
