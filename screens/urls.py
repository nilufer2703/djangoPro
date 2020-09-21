from django.urls import path

from . import views

urlpatterns = [path('',views.chat),
               path('login',views.login),
               path('home',views.home),
               path('personaldetails',views.personaldetail),
               path('homep_enroll',views.homep_enroll)
             ]