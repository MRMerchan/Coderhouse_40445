from itertools import permutations
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("about/", views.about, name="about"),
    path("salta/", views.salta, name="salta"),
    path("jujuy/", views.jujuy, name="jujuy"),
    path("mendoza/", views.mendoza, name="mendoza"),
    path("cataratas/", views.cataratas, name="cataratas"),
    path("perito/", views.perito, name="perito"),
    path("rioja/", views.rioja, name="rioja"),
    path("bariloche/", views.bariloche, name="bariloche"),
    path("santarosa/", views.santarosa, name="santarosa"),
    
    
    
] + staticfiles_urlpatterns()
