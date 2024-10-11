from django.contrib import admin
from django.urls import path, include
from .views import MusicList,music


urlpatterns = [
    # path("allmusic/",MusicList.as_view() ),
    path("allmusic/",MusicList),
    path("music/",music ,name='music'),
    # path("artistMusic/", ),

]