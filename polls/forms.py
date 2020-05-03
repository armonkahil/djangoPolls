from django import forms
from .models import Question, Choice
class CreateNewPoll(forms.Form):
  name = forms.CharField(label="Name", max_length=200)
  check = forms.BooleanField()
