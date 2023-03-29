from django.contrib import admin

# Register your models here.
from .models import Student


class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, MyModelAdmin)