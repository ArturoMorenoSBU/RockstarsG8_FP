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

#Get all Artist
@api_view(['GET'])
def getArtistOrBand(request):
    artist = ArtistOrBand.objects.all()
    serielizer = ArtistOrBandSerielizer(artist, many=True)
    return Response(serielizer.data)

#Get One Artist
@api_view(['GET'])
def getOneArtistOrBand(request, pk):
    artist = ArtistOrBand.objects.filter(_id=pk)
    serielizer = ArtistOrBandSerielizer(artist, many=True)
    return Response(serielizer.data)
  