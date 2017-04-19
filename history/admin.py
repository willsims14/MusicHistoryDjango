from django.contrib import admin

from .models import Artist, Album, Genre, Song

# from .models import Results

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Song)

