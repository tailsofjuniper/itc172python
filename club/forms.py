from django import forms
from .models import Meeting, MeetingMinutes

class MinutesForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'