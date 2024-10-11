from django.db import models
from django.contrib.auth.models import User



class Artist (models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ArtistName")
    bio = models.CharField(max_length=500,blank=True,null=True,default="NONE")
    def __str__(self) -> str:
        return f'{self.name}'


class Music(models.Model):
    Name = models.CharField(max_length=200,null=False,blank=False)
    Artist = models.ForeignKey(Artist,on_delete=models.RESTRICT,related_name="AritsitMusic")
    rank = models.IntegerField(default=0)
    cover = models.ImageField(upload_to='MusicCovers')
    def __str__(self) -> str:
        return f'{self.Name}{self.Artist}{self.rank}'


class comments(models.Model):
    text = models.CharField(max_length=500,null=False,blank=False)
    music = models.ForeignKey(Music,on_delete=models.SET_NULL,null=True,blank=True,related_name="AritsitMusic")
    def __str__(self) -> str:
        return f'{self.text}{self.music}'