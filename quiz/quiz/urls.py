from django.contrib import admin
from django.urls import path,include

urlpatterns = [
       
        path('quiz_admin/',include('quiz_admin.urls')),
        path('admin/', admin.site.urls),
]
