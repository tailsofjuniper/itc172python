from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingname = models.CharField(max_length=255)
    meetindate = models.DateField(max_length=255)
    meetingtime = models.TimeField(max_length=255)
    meetinglocation = models.CharField(max_length=255)
    meetingagenda = models.TextField()

    def __str__(self):
        return self.meetingname
 
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'
    

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    meetingattendance=models.CharField(max_length=255)
    minutestext=models.TextField()
    
    def __str__(self):
        return self.meetingid
 
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourceurl=models.CharField(max_length=255)
    resourcedateentered=models.DateField()
    minutestext=models.TextField()

    
    def __str__(self):
        return self.resourcename
 
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'