from django.contrib import admin

# Register your models here.

from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)