from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'quiz_admin/home.html')


def login_admin(request):
    return render(request, 'quiz_admin/login.html')


def admin_view_all_quiz(request):
    return render(request, 'quiz_admin/view_all_quiz.html')


def admin_add_quiz(request):
    return render(request, 'quiz_admin/add_quiz.html')

def admin_add_question(request):
    return render(request, 'quiz_admin/add_questions.html')
# Create your views here.
