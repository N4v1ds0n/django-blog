from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "author")
    search_fields = ["title", "content", "excerpt"]
    list_filter = ("status", "created_on", "author")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


# Register your models here.
admin.site.register(Comment)
