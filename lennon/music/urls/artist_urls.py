from django.urls import path
from music.views import artist_views as views
'''
This file is in charge of connecting views to our URLs
'''

urlpatterns = [

    path('', views.getArtistOrBand, name="artist"),
    path('<str:pk>/', views.getOneArtistOrBand, name="albumArtist"),

    
]
