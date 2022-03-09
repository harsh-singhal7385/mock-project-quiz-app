import re
from django.shortcuts import render, redirect, get_list_or_404
from datetime import datetime
from django.contrib import messages
from quiz_admin.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'quiz_user/register.html', context)


def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("login Success")
            return redirect('/quiz_user/')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'quiz_user/login.html')
    context = {}

    return render(request, 'quiz_user/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'quiz_user/index.html')


def fields(request, slug):
    pass


def javascript(request):
    data = "javascript"
    context = {
        "data": data
    }
    return render(request, 'quiz_user/showAllQuiz.html', context)


def python(request):
    data = "python"
    context = {
        "data": data
    }
    return render(request, 'quiz_user/showAllQuiz.html', context)


def cpp(request):
    data = "cpp"
    context = {
        "data": data
    }
    return render(request, 'quiz_user/showAllQuiz.html', context)


def java(request):
    data = "java"
    context = {
        "data": data
    }
    return render(request, 'quiz_user/showAllQuiz.html', context)


def userProfile(request):
    return render(request, 'quiz_user/profile.html')


def saveAnswers(request):
    pass


def questionsPage(request):

    details = {
        "name": "ABC XYZ",
        "subject_name": "Django / Flask",
        "total_marks": "10",
        "total_time": "10"
    }

    answers = [

    ]

    data = [
        {
            "question_id": 1,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
        {
            "question_id": 2,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
        {
            "question_id": 3,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
        {
            "question_id": 4,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
        {
            "question_id": 5,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
        {
            "question_id": 6,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
        {
            "question_id": 7,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
        {
            "question_id": 8,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
        {
            "question_id": 9,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
        {
            "question_id": 10,
            "question_description": "what is quantiphi?",
            "options": [{
                "option_1": "1",
                "option_2": "2",
                "option_3": "3",
                "option_4": "4"
            }],
            "correct_answer": "2",
            "marks": "1"
        },
    ]
    context = {"data": data, "details": details, "answers": answers}
    return render(request, 'quiz_user/questions.html', context)
