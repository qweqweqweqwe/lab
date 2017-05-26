from django.conf.urls import url
from .views import HomePageView, AboutPageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^about/$', AboutPageView.as_view(), name='about'),
]