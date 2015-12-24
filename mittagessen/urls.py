from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<esser_id>[0-9]+)/$', views.detail_by_id, name='detail_by_id'),
    # ex: /divar/adolf/
    url(r'^(?P<esser_team>[a-z]+)/(?P<esser_id_name>[a-z]+)/', views.detail_by_email, name='details_by_email'),
]