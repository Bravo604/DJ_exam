from django.contrib import admin
from .models import *


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'main_work', 'experience','get_level')
    search_fields = ('name',)
    list_filter = ('students',)
    fields = ('name', 'work_study_place', 'phone_number')

    @admin.display(description='Level')
    def get_level(self, obj):
        if obj.experience > 3:
            return f'middle'
        if obj.experience <= 3:
            return f'strong junior'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('language', 'mentor')
    fields = ('name', 'work_study_place', 'phone_number')
    list_display = ('name', 'date_started', 'student', 'mentor', 'language')
    search_fields = ('student__name', 'mentor__name')


admin.site.register(Language)
admin.site.register(Student)

