from django.conf.urls import url

from . import views

app_name = 'history'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index" ),
    url(r'^artists/', views.ArtistListView.as_view(), name="artists"),
    url(r'^songs/', views.SongListView.as_view(), name="songs"),
    url(r'^(?P<pk>[0-9]+)/$', views.ArtistDetailView.as_view(), name='detail'),

]