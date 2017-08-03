# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'sanfrancisco/$', views.SanFranciscoView.as_view()),
    url(r'oakland/$', views.OaklandView.as_view()),
    url(r'sanjose/$', views.SanJoseView.as_view()),
    url(r'richmond/$', views.RichmondView.as_view()),
    url(r'dalycity/$', views.DalyCityView.as_view()),
    url(r'cupertino/$', views.CupertinoView.as_view()),
    url(r'concord/$', views.ConcordView.as_view()),
    url(r'walnutcreek/$', views.WalnutCreekView.as_view()),
    url(r'redwoodcity/$', views.RedwoodCityView.as_view()),
    url(r'mountainview/$', views.MountainViewView.as_view()),
    
]
