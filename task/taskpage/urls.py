from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.home,name='home'),

    path('create_user/',views.create_user,name='create_user'),
    path('update_user/<int:pk>/',views.update_user,name='update_user'),
    path('delete_user/<int:pk>/',views.delete_user,name='delete_user'),

    path('add_comment',views.add_comment,name='add_comment'),
    path('delete_comment/<int:pk>',views.delete_comment,name='delete_comment'),
    
    path('create_task',views.create_task,name='create_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
    path('update_task/<int:pk>',views.update_task,name='update_task')
]