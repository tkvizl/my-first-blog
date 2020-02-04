from django.contrib import admin
from .models import Post, Comment, Question, Choice

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Choice)
