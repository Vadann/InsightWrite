from django.urls import path
from . import views

app_name = 'login_signup'
urlpatterns = [
    path('', views.LoginIndexView.as_view(), name='index'),
    path('<int:pk>/', views.LoginDetailView.as_view(), name='detail'),


    path('signup/', views.signup, name='signup'),
    path('', views.home),
    
    

]