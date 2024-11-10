from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Journal

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .journal_form import JournalForm

from datetime import datetime

# Journal views
class IndexView(generic.ListView):
    template_name = 'journals/index.html'
    model = Journal
    context_object_name = 'journals' 

class DetailView(generic.DetailView):
    template_name = 'journals/detail.html'

# Main Journal Entry webpage (Create/Read Journals)
def JournalEntries(request):
    submitted = False

    '''Utilizes a dictionary to add initial value for user ID 
       based on the current user's ID recorded auth_table in 
       the Railway Database so that each journal made is 
       specific to the current user logged in'''
    initial_dict = {'user_id': request.user.id}

    if(request.method == "POST"):
        form = JournalForm(request.POST, initial = initial_dict)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/journals/journal-entries?submitted=True')
    else:
        form = JournalForm(initial = initial_dict)
        if 'submitted' in request.GET:
            submitted = True

    '''Passes in the id of the current user ID that is logged in to the 
       website to show user specific journals'''
    journal_list = Journal.objects.filter(user_id = request.user.id).order_by('-journal_id').values()
    
    return render(request, 'journals/Journal Entries.html', {'form':form, 'submitted':submitted, 'journal_list':journal_list})


# Update Journal Entry page, redirects to JournalEntries view
def update_entry(request, journal_id):
    journal_entry = Journal.objects.get(pk=journal_id)
    form = JournalForm(request.POST or None, instance=journal_entry)
    if form.is_valid():
        form.save()
        return redirect('journals:journal_entries')
    return render(request, 'journals/update_entry.html', {'journal_entry': journal_entry, 'form':form})


# Delete a Journal Entry
def delete_entry(request, journal_id):
    journal_entry = Journal.objects.get(pk=journal_id)
    journal_entry.delete()
    return redirect('journals:journal_entries')    


#define custom view for the login page when log out
class CustomLoginRedirectView(LoginRequiredMixin, TemplateView):
    template_name = 'your_custom_login_redirect_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data you need here
        return context



# Class-based view for the weather page
class WeatherView(TemplateView):
    template_name = 'journals/weather.html'


# Class-based view for the media page
class GalleryView(TemplateView):
    template_name = 'journals/gallery.html'

# Class-based view for the weather page
class CalendarView(TemplateView):
    template_name = 'journals/calendar.html'
