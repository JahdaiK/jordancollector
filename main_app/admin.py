from django.contrib import admin

# Register your models here.
from .models import Jordan, Task

admin.site.register(Jordan)
admin.site.register(Task)