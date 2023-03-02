from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StudentNew)
admin.site.register(CourseNew)

#----------------------------------------

admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Batch)