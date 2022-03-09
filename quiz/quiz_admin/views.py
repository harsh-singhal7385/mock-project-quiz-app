from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from quiz_admin.models import AddQuiz, Question
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def admin_home(request):
    # print(request.user)
    # if request.user.is_anonymous:
    #     return redirect("/quiz_admin")
    return render(request, 'quiz_admin/home.html')


def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("login Success")
            return redirect('quiz_admin/admin_home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'quiz_admin/login.html')

    context = {}
    return render(request, 'quiz_admin/login.html', context)


def logout_admin(request):
    logout(request)
    return redirect('login')


def admin_view_all_quiz(request):
    return render(request, 'quiz_admin/view_all_quiz.html')


def admin_add_quiz(request):
    if request.method == "POST":
        quizId = request.POST.get('quizId')
        subject_name = request.POST.get('subject_name')
        instructor_name = request.POST.get('instructor_name')
        category = request.POST.get('category')
        # desc = request.POST.get('desc')
        quiz_time = request.POST.get('quiz_time')
        addQuiz = AddQuiz(quizId=quizId, subject_name=subject_name,
                          instructor_name=instructor_name, category=category, quiz_time=quiz_time, date=datetime.today())

        addQuiz.save()
        print("Data added")
        messages.success(request, 'Your Quiz has been created successfully!')
        return redirect('admin_add_question', pk=quizId)

    return render(request, 'quiz_admin/add_quiz.html')


def admin_add_question(request, pk):
    if request.method == "POST":
        quizId = pk
        question = request.POST.get('question')
        option_a = request.POST.get('option_a')
        option_b = request.POST.get('option_b')
        option_c = request.POST.get('option_c')
        option_d = request.POST.get('option_d')
        marks = request.POST.get('marks')
        answer = request.POST.get('answer')

        question = Question(quizId=quizId, question=question,
                            option_a=option_a, option_b=option_b, option_c=option_c, option_d=option_d, marks=marks, answer=answer)

        question.save()
        print("Question added")
        messages.success(request, 'Your have added a question')

    return render(request, 'quiz_admin/add_questions.html')
