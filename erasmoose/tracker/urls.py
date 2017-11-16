from django.conf.urls import url

from .views import moose_create, moose_detail


urlpatterns = [
    url(r'^create/$', moose_create, name="moose_create"),
    url(r'^(?P<pk>\d+)/$', moose_detail, name="moose_detail"),
]