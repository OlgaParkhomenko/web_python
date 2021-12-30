from django.contrib import admin
from .models import Post, Like


class LikeInline(admin.TabularInline):
    model = Like
    fk_name = 'post'


class PostAdmin(admin.ModelAdmin):
    inlines = [
        LikeInline,
    ]
    list_display = 'title', 'user', 'created_at'


admin.site.register(Post, PostAdmin)
