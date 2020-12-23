from django.contrib import admin
from django.urls import path,include
from app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup')


]
