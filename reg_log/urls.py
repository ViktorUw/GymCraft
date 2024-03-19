from django.urls import path

from . import views
urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("registration/", views.user_registration, name='registration'),
    path("login/", views.user_login, name='login')
]