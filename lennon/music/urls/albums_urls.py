from django.urls import path
from music.views import albums_views as views
'''
This file is in charge of connecting views to our URLs
'''

urlpatterns = [

    path('<str:pk>/', views.getAlbum, name="album"),
    path('artist/<str:pk>/', views.getArtistAlbums, name="albumArtist"),    
    path('songs/<str:pk>/', views.getAlbumSongs, name="albumSongs"),    
    path('code/p/<str:pk>', views.getAlbumsCodeP, name="codeAlbumsP"),
    path('', views.getAlbums, name="albums"),    
    path('code/v/<str:pk>', views.getAlbumsCodeV, name="codeAlbumsV"),
    
]