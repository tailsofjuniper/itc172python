from .models import Meeting, MeetingMinutes, Resource, Event
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'club/index.html')
def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resource.html' ,{'resource_list' : resource_list})