from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts.html', views.contacts, name='contacts'),
    path('deals.html', views.deals, name='deals'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
]