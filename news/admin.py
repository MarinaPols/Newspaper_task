from django.contrib import admin
#D3
from .models import Author, Category, Post, PostCategory, Comment, CategorySubscribers

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CategorySubscribers)
# Register your models here.
