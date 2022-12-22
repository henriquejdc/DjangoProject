from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .forms import SearchForm
from ..accounts.models import Profile


def comments_home(request):
    template_name = 'comments/comments_home.html'
    template_name_results = 'comments/user_search_results.html'
    context = {}
    form = SearchForm()
    query = request.GET.get('query', None)
    if query:
        profiles = Profile.objects.search(query)
        print(profiles)
        if profiles:
            context['profiles'] = profiles
            return render(request, template_name_results, context)
        else:
            messages.warning(request, _('No profile found'))
    context['form'] = form
    return render(request, template_name, context)
