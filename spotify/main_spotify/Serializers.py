from rest_framework import serializers
from .models import Artist
from .models import Album
from .models import Track

from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"
