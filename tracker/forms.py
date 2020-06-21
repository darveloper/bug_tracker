from django import forms
from .models import Ticket
from accounts.models import User 
 
class TicketForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=100)
    

class EditTicketForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=100)
    assigned_to = forms.ModelChoiceField(queryset=User.objects.all())