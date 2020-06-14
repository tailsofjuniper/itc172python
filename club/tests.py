import unittest
from meeting import Meeting
from meetingdetail import MeetingDetail
from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your tests here.
class MeetingTypeTest(TestCase):
    def setup(self):
        type = Meeting(typename='Anniversary')
        
    def test_string(self):
        type=Meeting