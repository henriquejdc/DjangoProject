from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _

from .forms import SearchForm, CommentForm
from .models import Comment
from ..accounts.models import Profile


@login_required
def comments_home(request):
    template_name = 'comments/comments_home.html'
    template_name_results = 'comments/user_search_results.html'
    context = {}
    form = SearchForm()
    query = request.GET.get('query', None)
    if query:
        profiles = Profile.objects.search(query)
        if profiles:
            context['profiles'] = profiles
            return render(request, template_name_results, context)
        else:
            messages.warning(request, _('No profile found'))
    context['form'] = form
    return render(request, template_name, context)


@login_required
def get_user_profile_add_comment(request, username):
    template_name = 'comments/get_user_profile_add_comment.html'
    user_profile = get_object_or_404(Profile, user__username=username)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user_profile.user
            f.save()
            messages.success(request, _('Feedback added successfully'))
            return redirect('comments:comments_home')
    form = CommentForm()
    context = {
        'form': form,
        'user_profile': user_profile
    }
    return render(request, template_name, context)


@login_required
def comment_details(request, id_comment):
    comment = get_object_or_404(Comment, pk=id_comment)
    template_name = 'comments/comment_details.html'
    context = {}

    if comment.user == request.user:
        comment.read = True
        comment.save()
        context['comment'] = comment
    else:
        messages.error(request, _('You cannot view this feedback.'))

    return render(request, template_name, context)
