from django.contrib import admin

from blog.models import Category, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'slug']
