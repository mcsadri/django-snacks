# define the routes

from django.urls import path

from .views import HomePageView

# urlpatterns = required name for django
urlpatterns = [
    # pattern = (''routeasastring', callbackfunction, name='doodah')
    path('', HomePageView.as_view(), name='home'),
]
