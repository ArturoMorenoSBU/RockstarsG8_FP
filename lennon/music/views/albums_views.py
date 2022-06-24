from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..models import *
from ..serializers import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data
        

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Get all albums
@api_view(['GET'])
def getAlbums(request):
    albums = Album.objects.all()
    serielizer = AlbumSerializer(albums, many=True)
    return Response(serielizer.data)

#Get all Albums by artist
@api_view(['GET'])
def getArtistAlbums(request, pk):
    artist = Album.objects.filter(artist=pk)
    serielizer = AlbumSerializer(artist, many=True)
    return Response(serielizer.data)

#Get all Albums by codeP
@api_view(['GET'])
def getAlbumsCodeP(request, pk):
    albums = Album.objects.filter(codeP=pk)
    serielizer = AlbumSerializer(albums, many=True)
    return Response(serielizer.data)

#Get all Albums by codeV
@api_view(['GET'])
def getAlbumsCodeV(request, pk):
    albums = Album.objects.filter(codeV=pk)
    serielizer = AlbumSerializer(albums, many=True)
    return Response(serielizer.data)

#Get all Albums    
@api_view(['GET'])
def getAlbum(request, pk):
    album = Album.objects.filter(_id=pk)
    serielizer = AlbumSerializer(album, many=True)
    return Response(serielizer.data)


#Get All Songs by Album
@api_view(['GET'])
def getAlbumSongs(request, pk):
    song = Song.objects.filter(album=pk)
    serielizer = SongSerielizer(song, many=True)
    return Response(serielizer.data)


