
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login_admin, name="admin_login"),
    path('admin_view_all_quiz/', views.admin_view_all_quiz,
         name='admin_view_all_quiz'),
    path('admin_add_quiz/', views.admin_add_quiz, name='admin_add_quiz'),
    path('admin_add_question/<str:pk>', views.admin_add_question,
         name='admin_add_question'),
    path('admin_veiw_questions/<id>', views.admin_view_questions,
         name='admin_view_questions'),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('logout/', views.logout_admin, name="admin_logout"),
    path('admin_delete_quiz/<id>', views.admin_delete_quiz,
         name='admin_delete_quiz'),
    path('admin_delete_question/<id>', views.admin_delete_question,
         name='admin_delete_question'),
    path('admin_update_question/<id>', views.admin_update_question,
         name='admin_update_question'),
    path('admin_update_quiz/<id>', views.admin_update_quiz,
         name='admin_update_quiz'),

]
