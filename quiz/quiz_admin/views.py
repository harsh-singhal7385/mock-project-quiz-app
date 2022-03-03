from django.shortcuts import render
from django.http import HttpResponse


def login_admin(request):
    return render(request, 'quiz_admin/login.html')


def home_admin(request):
    return render(request, 'quiz_admin/home.html')
def admin_dashboard(request):
    return render(request,'quiz_admin/dashboard.html')
# Create your views here.
