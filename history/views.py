from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Artist, Album, Genre, Song


# Create your views here.
class ArtistListView(generic.ListView):
    # model = Artist
    template_name = 'history/artist_list.html'
    model = Artist
    context_object_name = 'artists'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Artist.objects.order_by('name')
        return Artist.objects.all()

class SongListView(generic.ListView):
    # model = Artist
    template_name = 'history/song_list.html'
    model = Song
    context_object_name = 'songs'

    def get_queryset(self):
        """Return the last five published questions."""
        return Song.objects.all()


class IndexView(generic.ListView):
    template_name = 'history/index.html'
    model = Artist
    context_object_name = 'artists'

    def get_queryset(self):
        """Return the last five published questions."""

        return HttpResponse("Hello, world. You're at the history index.")

class ArtistDetailView(generic.DetailView):
    model = Artist
    template_name = 'history/detail.html'
    context_object_name = 'artist'

    # def get_queryset(self, songId):
    #     """Return the last five published questions."""
    #     return Artist.objects.filter('id'==songId).order_by('name')

# def x(request, artist_id):
#     artist = get_object_or_404(Artist, pk=artist_id)
#     return render(request, 'history/detail.html', {
#         'artist': artist,
#         'error_message': "You didn't select a choice.",
#     })
