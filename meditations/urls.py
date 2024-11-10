from django.urls import path
from . import views

app_name = 'meditations'
urlpatterns = [
    path('', views.MeditationsIndexView.as_view(), name='index'),
    path('<int:pk>/', views.MeditationsDetailView.as_view(), name='detail'),

    
]