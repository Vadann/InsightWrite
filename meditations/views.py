from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Meditation

class MeditationsIndexView(generic.ListView):
    template_name = 'meditations/index.html'
    model = Meditation
    context_object_name = 'meditations' 

class MeditationsDetailView(generic.DetailView):
    template_name = 'meditations/detail.html'
