from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resource/', views.getresource, name='resource'),
    path('meeting/', views.getmeeting, name='meeting'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    # path('minutes/', views.getminutes, name='minutes')
    # path('event/', views.getevent, name='event')
]