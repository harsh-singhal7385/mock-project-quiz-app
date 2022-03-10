from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class AddQuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name',
                    'instructor_name', 'category', 'quiz_time', 'date')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'quizId', 'marks')


admin.site.register(AddQuiz, AddQuizAdmin)
admin.site.register(Question, QuestionAdmin)
