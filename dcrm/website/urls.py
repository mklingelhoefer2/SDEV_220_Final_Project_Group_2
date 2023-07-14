from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('contact/', views.contact, name='contact'),
    path('deal/', views.deal, name='deal'),
    path('add_deal/', views.add_deal, name='add_deal'),
    path('deal/<int:pk>', views.deal_record, name='deal_record'),
    path('update_deal/<int:pk>', views.update_deal, name='update_deal'),
    path('delete_deal/<int:pk>', views.delete_deal, name='delete_deal'),
]

