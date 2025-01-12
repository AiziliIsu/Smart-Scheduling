from django.contrib import admin
from .models import *

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'duration', 'scaler_value')
    inlines = [LessonInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'lesson_type', 'times_per_week')
    list_filter = ('lesson_type',)

admin.site.register(Individual)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)









