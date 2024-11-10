from django import forms
from django.forms import ModelForm
from .models import Journal     #calls models.py and gets Journal table


#create a journal form
class JournalForm(ModelForm):
    #Django-specific class for defining actions
    class Meta:
        model = Journal
        # fields = "__all__" #calls all fields in Journal
        fields = ('user_id', 'tag_id', 'title', 'content')
        labels = {
            'user_id': '',
            'tag_id': '',
            'title': '',
            'content': '',
        }
        #attaches bootstrap onto form fields for styling
        widgets = {
            'user_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'User ID'}),
            'tag_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tag ID'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title here'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write your journal entry here'}),
        }