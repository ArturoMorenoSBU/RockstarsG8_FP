from django.urls import path
from music.views import playlist_views as views
'''
This file is in charge of connecting views to our URLs
'''

urlpatterns = [
    path('', views.getPlayLists, name="playlists"),
    #path('user/playlist/<str:pk>/', views.getPlayListUser, name="album"),
]


