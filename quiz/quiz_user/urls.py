from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('login/', views.login_admin, name="login"),
    path('profile/', views.userProfile, name="userProfile"),
    path('submitanswer/', views.submitAnswers, name="submitAnswers"),
    path('test_questions_page/', views.questionsDemoPage, name="questionsDemoPage"),
    path('test_questions_page/<str:slug>/', views.questionsPage, name="questionsPage"),
    path('showquiz/', views.showAllQuiz, name="showAllQuiz"),
    path('showquiz/<str:slug>/', views.showQuiz, name="showQuiz"),
    path('showquiz/<str:slug>/test_questions_page/<str:slug2>', views.questionsPage, name="questionsPage"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path('score/',views.score, name = "score"),
    path('leaderboard/',views.leaderboard, name = "leaderboard"),
    
]
