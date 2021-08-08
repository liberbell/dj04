from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.app_homepage, name="app_homepage"),
    path("about_us", views.about_us, name="about_us")
]
