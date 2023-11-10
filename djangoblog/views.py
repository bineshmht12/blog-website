from django.views.generic import View
from django.shortcuts import render

from blog.models import Category, Blog


class HomePageView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        blogs = Blog.objects.all()
        context = {
            'categories': categories,
            'blogs': blogs
        }
        return render(request, self.template_name, context)
