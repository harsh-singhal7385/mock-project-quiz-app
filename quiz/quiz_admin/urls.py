
from django.urls import path,include
from . import views
urlpatterns = [
       path('',views.login_admin,name="login"),
    path('admin_home/',views.home_admin,name="home")
]
