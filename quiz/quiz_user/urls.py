from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_admin, name="login"),
    path('profile/', views.userProfile, name="userProfile"),
    path('test_questions_page/', views.questionsPage, name="questionsPage"),
    path('javascript/', views.javascript, name="javascript"),
    path('python/', views.python, name="python"),
    path('java/', views.java, name="java"),
    path('cpp/', views.cpp, name="cpp"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logout_user, name="logout"),

]
