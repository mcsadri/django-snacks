# define the routes

from django.urls import path

from .views import HomePageView, AboutView

# urlpatterns = required name for django
urlpatterns = [
    # pattern = (''routeasastring', callbackfunction, name='doodah')
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
]
