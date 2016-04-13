from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^compare/(?P<benchmark_id1>[0-9]+)/(?P<benchmark_id2>[0-9]+)$', views.compare, name='compare'),
    url(r'^compare/(?P<benchmark_id1>[0-9]+)/(?P<benchmark_id2>[0-9]+)\.json', views.compare_json, name='compare_json'),
    url(r'^upload', views.upload, name='upload'),
]