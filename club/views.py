from .models import Meeting, MeetingMinutes, Resource, Event
from django.shortcuts import render, get_object_or_404
from .forms import MinutesForm

# Create your views here.
def index (request):
    return render(request, 'club/index.html')
def getresource (request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resource.html' ,{'resource_list' : resource_list})
def getmeeting (request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meeting.html' ,{'meeting_list' : meeting_list})
def meetingdetails (request, id):
    meeting_detail=get_object_or_404(Meeting, pk=id)
    meeting_location=meeting_detail.meetinglocation
    # discount=prod.memberdiscount
    meeting_agenda=meeting_detail.meetingagenda
    # agenda=Meeting.objects.filter(meetingagenda=id).count()
    context={
        'meeting_detail' : meeting_detail,
        'meeting_location' : meeting_location,
        'meeting_agenda' : meeting_agenda,
    }
    return render(request, 'club/meetingdetails.html', context=context)
def meetingminutes(request):
     form=MinutesForm
     if request.method=='POST':
          form=MinutesForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MinutesForm()
     else:
          form=MinutesForm()
     return render(request, 'club/minutes.html', {'form': form})
