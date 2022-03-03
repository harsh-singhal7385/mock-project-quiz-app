from django.contrib import admin
from django.urls import path,include

urlpatterns = [
       
        path('',include('quiz_admin.urls')),
        path('admin/', admin.site.urls),
]
