from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView
from itertools import permutations
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views


urlpatterns = [
    path("salta/", views.salta, name="salta"),
    path("jujuy/", views.jujuy, name="jujuy"),
    path("mendoza/", views.mendoza, name="mendoza"),
    path("cataratas/", views.cataratas, name="cataratas"),
    path("perito/", views.perito, name="perito"),
    path("rioja/", views.rioja, name="rioja"),
    path("bariloche/", views.bariloche, name="bariloche"),
    path("santarosa/", views.santarosa, name="santarosa"),
    ] + staticfiles_urlpatterns()

    