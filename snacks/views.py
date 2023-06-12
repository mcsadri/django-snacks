# what's "invoked" when a user visits the site, similar in function to an Express callback function

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
