from django.contrib import admin

# Register your models here.

from .models import *

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1  # Number of empty lesson forms to display by default

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'duration', 'is_mandatory', 'scaler_value')  # Fields to display in list view
    inlines = [LessonInline]  # Allows adding lessons inline within course form

class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'lesson_type', 'times_per_week')  # Fields to display in list view
    list_filter = ('lesson_type',)  # Add a filter for lesson type



admin.site.register(Individual)
admin.site.register(Classroom)
admin.site.register(Schedule)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)









