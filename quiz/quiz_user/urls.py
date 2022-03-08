from django.urls import path, include
from . import views

urlpatterns = [

    path('profile/' , views.userProfile , name = "userProfile"),
    path('test_questions_page/', views.questionsPage, name = "questionsPage" )
] 