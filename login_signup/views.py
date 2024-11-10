from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import FormView
from .models import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from django.shortcuts import render, redirect



# Login_signup views

def home(request):
    return render(request, "index.html")


class LoginIndexView(FormView):
    template_name = 'login_signup/index.html'
    form_class = LoginForm
    success_url = '/success'  # replace with your actual success url

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)  # Use the authenticate function
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
class LoginDetailView(generic.DetailView):
    template_name = 'login_signup/detail.html'
    form_class = LoginForm
    success_url = '/success'  # replace with your actual success url

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)  # Use the authenticate function
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
def signup(request):
    return render(request, 'login_signup/Sign-up.html')


