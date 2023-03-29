from django.contrib import admin
from .models import Question
from .models import Course
from .models import Result

# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, MyModelAdmin)

class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, MyModelAdmin)

class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Result, MyModelAdmin)


