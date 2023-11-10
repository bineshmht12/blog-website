from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from blog.models import Blog


class BlogDetailsPageView(View):
    template_name = 'blog/details.html'
    
    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, slug=self.kwargs['slug'])
        context = {
            'blog': blog
        }
        return render(request, self.template_name, context)
