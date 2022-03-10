
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login_admin, name="login"),
    path('admin_view_all_quiz/', views.admin_view_all_quiz,
         name='admin_view_all_quiz'),
    path('admin_add_quiz/', views.admin_add_quiz, name='admin_add_quiz'),
    path('admin_add_question/<str:pk>', views.admin_add_question,
         name='admin_add_question'),
     path('admin_veiw_questions/<id>', views.admin_view_questions,name='admin_view_questions'),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('logout/', views.logout_admin, name="logout"),

]
