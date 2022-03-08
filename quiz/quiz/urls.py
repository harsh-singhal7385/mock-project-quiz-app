from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('quiz_admin/' , include('quiz_admin.urls')),
    path('quiz_user/' , include('quiz_user.urls')),
  
    path('admin/', admin.site.urls),
]
