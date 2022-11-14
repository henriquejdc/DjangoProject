from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'home/index.html'

#     def get(self, request):
#         return render(request, 'base.html', {})
#
#
# def home_view(request):
#     return render(request, 'base.html', {})
