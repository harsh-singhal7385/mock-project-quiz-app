import re
from traceback import print_tb
from unicodedata import category
from django.shortcuts import render, redirect, get_list_or_404
from datetime import datetime
from django.contrib import messages
from django.urls import reverse
from quiz_admin.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from quiz_admin.models import AddCategory, AddQuiz, QuestionDemo
from quiz_user.models import ScoreCard,LeaderBoard
from json import dumps
from django.http import JsonResponse
count = 0

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
            print("login Success",user)
            return redirect('/quiz_user/')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'quiz_user/login.html')
    context = {}

    return render(request, 'quiz_user/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def home(request):
    # print(request.user)
    # print(request.user.id)
    # print(request.user.is_authenticated)
    print("inside home of quiz_user")
    print(" quiz_user")
    print("inside home ")
    data = AddCategory.objects.all()
    data1 = AddQuiz.objects.all()
    
    
    if (request.user.is_authenticated):
        print("innn")
        context = {
        "data" : data,
        "data1" : data1,
        "user" : request.user
    }
        return render(request, 'quiz_user/index.html',context)
    else:
        print("outt")
        context = {
        "data" : data,
        "data1" : data1,
    }
        return render(request, 'quiz_user/index.html',context)


def fields(request, slug):
    pass


def showAllQuiz(request):
    data = AddQuiz.objects.all()
    print(data)
    if (request.user.is_authenticated):
       
        context = {
        "data" : data,
        "user" : request.user
    }
        return render(request, 'quiz_user/showAllQuiz.html',context)
    else:
       
        
        return redirect('home')

def showQuiz(request,slug):
    print(slug)
    data = AddQuiz.objects.filter(category = slug).all()
    print(data)
    if (request.user.is_authenticated):
       
        context = {
        "data" : data,
        "user" : request.user
    }
        return render(request, 'quiz_user/showAllQuiz.html', context)
    
    else:
       
        return redirect('home')


def userProfile(request):
    getdata = ScoreCard.objects.all()
    if (request.user.is_authenticated):
       
        context = {
        "data" : getdata,
        "user" : request.user
    }
        return render(request , 'quiz_user/profile.html',context)
    
    else:
       
        return redirect('home')

    

def score(request):
    getdata = ScoreCard.objects.all()

    if (request.user.is_authenticated):
       
        context = {
        "data" : getdata,
        "user" : request.user
    }
        return render(request , 'quiz_user/score.html',context)
    
    else:
       
        return redirect('home')


def leaderboard(request):
    getdata = ScoreCard.objects.all()
    
    if (request.user.is_authenticated):
       
        context = {
        "data" : getdata,
        "user" : request.user
    }
        return render(request , 'quiz_user/leaderboard.html',context)
    
    else:
 
        return redirect('home')


def submitAnswers(request):
    if request.method == "GET":
        score = request.GET.get('score')  ###['score']
        subjectname = request.GET.get('subjectname')  ###['subjectname']
        nosofquestions = request.GET.get('nosofquestions')  ###['nosofquestions']
        
        score_data = ScoreCard(score = score, subject_name = subjectname)
        score_data.save()
        
        score_data = ScoreCard.objects.filter(score = score, subject_name = subjectname).all()
        print(score_data)
        
        return render(request,'quiz_user/score.html',{"score_data":score_data})
    #     return JsonResponse({
    #             'success': True,
    #             'url': reverse('score'),
    #         })
    # return JsonResponse({ 'success': False })

def questionsDemoPage(request):
    
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

    
def questionsPage(request,slug):
    if (request.user.is_authenticated == False):
        return redirect('home')
    else:
        
        print("inside questions")
        total_time = 0
        answers = {}
        dat = {}
        data = QuestionDemo.objects.filter(subject_name = slug).all()
        count = len(data)
        sum = 0
        subject_name = ""
        j = 1
        for i in data:
            sum += i.marks
            dat = {j : i.answer}
            answers.update(dat)
            j+=1
        
        duration = AddQuiz.objects.filter(subject_name = slug).all()
        for i in duration:
            total_time = i.quiz_time
            subject_name = i.subject_name
        # data=""
        details = {
            "name": "ABC XYZ",
            "subject_name": subject_name,
            "total_marks": sum,
            "total_time": total_time
        }
        
        dataJSON = dumps(answers)
        nosOfQ = dumps(count)
        subjectName = dumps(subject_name)
        

        context = {"data": data, "details": details, "answers": dataJSON,"nosOfQ" : nosOfQ,"subjectName" :subjectName,"sum" : sum }
        return render(request, 'quiz_user/questions.html', context)
