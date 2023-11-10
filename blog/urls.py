from django.urls import path

from blog.views import BlogDetailsPageView

app_name = 'blog'

urlpatterns = [
    path('<slug:slug>/', BlogDetailsPageView.as_view(), name='details'),
]
