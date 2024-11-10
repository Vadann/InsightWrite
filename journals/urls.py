from django.urls import path
from . import views

from .views import CustomLoginRedirectView

from .views import WeatherView
from .views import GalleryView
from .views import CalendarView

app_name = 'journals'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    #configure the URL pattern for the /journal-entries page
    path('journal-entries/', views.JournalEntries, name='journal_entries'),

    #configure the URL pattern for the /update_entry page
    path('update_entry/<journal_id>', views.update_entry, name='update-entry'),

    #configure the URL pattern for the /delete_entry (pseudo) page,
    #merely redirects back to journal_entries after deletion
    path('delete_entry/<journal_id>', views.delete_entry, name='delete-entry'),


    #configure the URL pattern for the /custom_logout_page
    path('custom_login_redirect/', CustomLoginRedirectView.as_view(), name='custom_login_redirect'),


    #configure the URL pattern for the weather page
    # In journals/urls.py
    path('weather/', WeatherView.as_view(), name='weather'),

    path('gallery/', GalleryView.as_view(), name='gallery'),

    path('calendar/', CalendarView.as_view(), name='calendar'),
]