from django.contrib import admin

from .models import Post, PostAttachment


admin.site.register(Post)
admin.site.register(PostAttachment)