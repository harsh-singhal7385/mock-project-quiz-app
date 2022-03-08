from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/' , views.userProfile , name = "userProfile"),
    path('test_questions_page/', views.questionsPage, name = "questionsPage" )
] 