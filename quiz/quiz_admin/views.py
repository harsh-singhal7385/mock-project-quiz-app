from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from quiz_admin.models import AddQuiz, Question
from django.contrib import messages
from quiz_admin.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .forms import QuestionForm

def admin_home(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/quiz_admin")
    return render(request, 'quiz_admin/home.html')


def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("login Success")
            return redirect('admin_home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'quiz_admin/login.html')
    context = {}

    return render(request, 'quiz_admin/login.html', context)


def logout_admin(request):
    logout(request)
    return redirect('admin_login')


@login_required(login_url='admin_login')
def admin_view_all_quiz(request):
    context = {}
    context["dataset"] = AddQuiz.objects.all()
    return render(request, 'quiz_admin/view_all_quiz.html', context)


@login_required(login_url='admin_login')
def admin_add_quiz(request):
    if request.method == "POST":
        # quizId = request.POST.get('quizId')
        subject_name = request.POST.get('subject_name')
        instructor_name = request.POST.get('instructor_name')
        category = request.POST.get('category')
        # desc = request.POST.get('desc')
        quiz_time = request.POST.get('quiz_time')
        addQuiz = AddQuiz(subject_name=subject_name,
                          instructor_name=instructor_name, category=category, quiz_time=quiz_time, date=datetime.today())

        addQuiz.save()
        # print("Data added")
        # messages.success(request, 'Your Quiz has been created successfully!')
        return redirect('admin_add_question', pk=addQuiz.id)

    return render(request, 'quiz_admin/add_quiz.html')


@login_required(login_url='admin_login')
def admin_add_question(request, pk):
    if 'save_and_add' in request.POST:
        quizId = AddQuiz.objects.get(id=pk)
        question = request.POST.get('question')
        option_a = request.POST.get('option_a')
        option_b = request.POST.get('option_b')
        option_c = request.POST.get('option_c')
        option_d = request.POST.get('option_d')
        marks = request.POST.get('marks')
        answer = request.POST.get('answer')
        question = Question(quizId=quizId, question=question, option_a=option_a,
                            option_b=option_b, option_c=option_c, option_d=option_d, marks=marks, answer=answer)

        question.save()
        # print("Question added")
       # messages.success(request, 'Your have added a question')
        return redirect('admin_add_question', pk=pk)
    
    if 'save' in request.POST:
        quizId = AddQuiz.objects.get(id=pk)
        question = request.POST.get('question')
        option_a = request.POST.get('option_a')
        option_b = request.POST.get('option_b')
        option_c = request.POST.get('option_c')
        option_d = request.POST.get('option_d')
        marks = request.POST.get('marks')
        answer = request.POST.get('answer')
        question = Question(quizId=quizId, question=question, option_a=option_a,
                            option_b=option_b, option_c=option_c, option_d=option_d, marks=marks, answer=answer)

        question.save()
        # print("Question added")
       # messages.success(request, 'Your have added a question')
        return redirect('admin_view_all_quiz')

    context = {'pk': pk}
    return render(request, 'quiz_admin/add_questions.html', context)



@login_required(login_url='admin_login')
def admin_view_questions(request, id):
    context = {}
    context["dataset"] = Question.objects.all().filter(quizId=id)
    return render(request, 'quiz_admin/admin_view_questions.html', context)


@login_required(login_url='admin_login')
def admin_delete_quiz(request, id):
    context = {}
    obj = get_object_or_404(AddQuiz, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('admin_view_all_quiz')

    return render(request, "quiz_admin/delete_view.html", context)


@login_required(login_url='admin_login')
def admin_delete_question(request, id):

    obj = get_object_or_404(Question, id=id)

    quizId = obj.quizId
    if request.method == "POST":
        obj.delete()
        return redirect('admin_view_questions', id=quizId)
    context = {
        'quizId': quizId
    }
    return render(request, "quiz_admin/delete_question_view.html", context)


@login_required(login_url='admin_login')
def admin_update_question(request, id):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
    quizId = obj.quizId
    # pass the object as instance in form
    form = QuestionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('admin_view_questions', id=quizId)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "quiz_admin/update_question_view.html", context)

@login_required(login_url='admin_login')
def admin_update_quiz(request, id):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(AddQuiz, id = id)
    quizId = obj.id
    # pass the object as instance in form
    form = QuizForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('admin_view_all_quiz')
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "quiz_admin/update_quiz.html", context)