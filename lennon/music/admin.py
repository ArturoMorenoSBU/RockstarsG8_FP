from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(ArtistOrBand)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)
admin.site.register(SongsPlaylist)
