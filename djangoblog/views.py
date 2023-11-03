from django.views.generic import View
from django.shortcuts import render

class HomePageView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
