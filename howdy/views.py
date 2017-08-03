# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class SanFranciscoView(TemplateView):
    template_name = "SanFrancisco.html"

class OaklandView(TemplateView):
    template_name = "Oakland.html"

class SanJoseView(TemplateView):
    template_name = "SanJose.html"

class RichmondView(TemplateView):
    template_name = "Richmond.html"

class DalyCityView(TemplateView):
    template_name = "DalyCity.html"

class CupertinoView(TemplateView):
    template_name = "Cupertino.html"

class ConcordView(TemplateView):
    template_name = "Concord.html"

class WalnutCreekView(TemplateView):
    template_name = "WalnutCreek.html"

class RedwoodCityView(TemplateView):
    template_name = "RedwoodCity.html"

class MountainViewView(TemplateView):
    template_name = "MountainView.html"
