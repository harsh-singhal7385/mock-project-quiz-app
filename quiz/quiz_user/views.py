import re
from django.shortcuts import render,redirect,get_list_or_404

# Create your views here.

def userProfile(request):
    return render(request,'quiz_user/profile.html')

def questionsPage(request):
    return render(request, 'quiz_user/questions.html')