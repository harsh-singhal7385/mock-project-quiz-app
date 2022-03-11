from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz_admin/', include('quiz_admin.urls')),
    path('quiz_user/', include('quiz_user.urls')),
    path('quiz_auth/', include('quiz_auth.urls')),
    path('', views.home_main, name="home_main"),
]
