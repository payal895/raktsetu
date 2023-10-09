from django.urls import path
from . import views

app_name = 'BloodProject'

urlpatterns = [
    path("", views.index, name="index"),
    path("service", views.service, name="service"),
    path("appointment", views.appointment, name="appointment"),
    path("blog", views.blog, name="blog"),
    path("about", views.about, name="about"),
    path("signup", views.handlesignup, name="signup"),
    path("login", views.handlelogin, name="login"),
    path("logout", views.handlelogut, name="handlelogout"),



]

