from django.contrib import admin
from .models import Comment,News
# Register your models here.
admin.site.register(Comment)
admin.site.register(News)