# what's "invoked" when a user visits the site, similar in function to an Express callback function

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    # db retreival emulation of 'snacks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # assign a list of t a key calls "snacks" inside of context
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/53/Grapes%2C_Rostov-on-Don%2C_Russia.jpg",
                "title": "Grapes",
                "description": "A grape is a fruit, botanically a berry, of the deciduous woody vines of the "
                               "flowering plant genus Vitis. Grapes are a non-climacteric type of fruit, "
                               "generally occurring in clusters.",
                "reference_url": "https://en.wikipedia.org/wiki/Grape"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a8/M%26m2.jpg",
                "title": "Peanut m&m's",
                "description": "M&M's (stylized as m&m's) are multi-colored button-shaped chocolates, each of which "
                               "has the letter 'm' printed in lower case in white on one side, consisting of a candy "
                               "shell surrounding a filling which varies depending upon the variety of M&M's.",
                "reference_url": "https://en.wikipedia.org/wiki/M%26M%27s",
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Scotland_Haggis.jpg",
                "title": "Haggis",
                "description": "Haggis is a savoury pudding containing sheep's pluck (heart, liver, and lungs), "
                               "minced with onion, oatmeal, suet, spices, and salt, mixed with stock, and cooked "
                               "traditionally encased in the animal's stomach.",
                "reference_url": "https://en.wikipedia.org/wiki/Haggis",
            }
        ]

        return context
