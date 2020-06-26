from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(todo)
admin.site.register(todoweek)
admin.site.register(todomonth)