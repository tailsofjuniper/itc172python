from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.
class MeetingAgendaTest(TestCase):
    def setup(self):
        agenda = Meeting(meetingname='Wine Club')
        meeting=Meeting(meetingname='Wine Club', meetingagenda=agenda, meetingdate=9-7-2020)

    def test_string(self):
       agenda=Meeting(meetingname='Wine Club')
       self.assertEqual(str(type), agenda.meetingname)

    def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meetingagenda')