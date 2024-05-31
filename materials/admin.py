from django.contrib import admin

from materials.models import Course, Lesson, Subscribe

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Subscribe)
