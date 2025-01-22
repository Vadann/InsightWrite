from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import FormView
from .models import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from django.shortcuts import render, redirect



# Login_signup views

def home(request):
    return render(request, "index.html")


class LoginIndexView(View):
    template_name = 'login_signup/index.html'
    
    def get(self, request):
        login_form = LoginForm()
        signup_form = SignUpForm()
        return render(request, self.template_name, {
            'login_form': login_form,
            'signup_form': signup_form
        })
    
    def post(self, request):
        if 'login' in request.POST:
            form = LoginForm(data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('username')  # Form uses username field for email
                password = form.cleaned_data.get('password')
                try:
                    user = User.objects.get(email=email)
                    user = authenticate(request, username=user.username, password=password)
                    if user is not None:
                        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                        return redirect('journals:index')
                except User.DoesNotExist:
                    pass
                messages.error(request, "Invalid email or password.")
            return render(request, self.template_name, {
                'login_form': form,
                'show_login': True  # Add this to keep login form visible
            })
            
        elif 'signup' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                try:
                    user = form.save()
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('journals:index')
                except Exception as e:
                    print(f"Error creating user: {e}")
                    messages.error(request, "Error creating account. Please try again.")
            else:
                if 'email' in form.errors:
                    messages.error(request, "Email already exists")
                if 'password2' in form.errors:
                    messages.error(request, "Passwords don't match")
            return render(request, self.template_name, {
                'signup_form': form,
                'show_signup': True
            })


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


