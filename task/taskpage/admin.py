from django.contrib import admin

# Register your models here.
from .models import Task, Comment,User

admin.site.register(Task)


admin.site.register(Comment)


admin.site.register(User)