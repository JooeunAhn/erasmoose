from django.conf.urls import url

from .views import moose_create, moose_detail, about_us, stat


urlpatterns = [
    url(r'^create/$', moose_create, name="moose_create"),
    url(r'^(?P<pk>\d+)/$', moose_detail, name="moose_detail"),
    url(r'^about_us/$', about_us, name="about_us"),
    url(r'^stat/$', stat, name="stat")
]
