"""spotify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_spotify.views import *
from django.urls import reverse
from rest_framework import routers
#from rest_framework_simplejwt import TokenObtainPairView,


router = routers.SimpleRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'track', TrackViewSet )
router.register(r'playlist', PlaylistViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v2/', include(router.urls)),
    path('api/v3/', include(router.urls)),
    path('api/v4/', include(router.urls)),

    ##  path('main/', include('main_spotify.urls', namespace='main'))
    # path('api/v1/artists/', ArtistViewSet.as_view({'get':'list'})),
    # path('api/v2/album/', AlbumApiList.as_view()),
    # path('api/v1/artists/<int:pk>', ArtistViewSet.as_view({'put': 'update'})),
    # path('api/v3/track/', TrackApiView.as_view()),
    # path('api/v4/playlist/', PlaylistApiView.as_view())

]
