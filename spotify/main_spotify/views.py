from django.shortcuts import render

from rest_framework.permissions import IsAdminUser
from rest_framework import generics, status
# Create your views here.
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .Serializers import *

from rest_framework import viewsets

## Artist api
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# ## Album api

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

## Track api

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

## Playlist api

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

# class PlaylistApiView(APIView):
#     def get(self, request):
#         w = Playlist.objects.all()
#         return Response({'posts': PlaylistSerializer(w, many=True).data})
#     def post(self, request):
#         serializer = TrackSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request=Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response={
                "message": "User created, good job",
                "data" : serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)










