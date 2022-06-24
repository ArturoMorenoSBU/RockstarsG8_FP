import random
from django.db import models
from django.contrib.auth.models import User
from pytz import country_names

# Create your models here.
def random_string():
    return str(random.randint(10000, 99999))


class ArtistOrBand(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name= models.CharField(max_length=200, null=True, blank=True)
    country= models.CharField(max_length=200, null=True, blank=True)
    image = models.TextField(null = True, blank=True)
    

    #Constructor to display the artist name
    def __str__(self):
        return str(self.name)

class Genre(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    genre= models.CharField(max_length=200, null=True, blank=True)
    
    
    #Constructor to display the artist name
    def __str__(self):
        return str(self.genre)



class Album(models.Model):
    user= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title=models.CharField(max_length=200, null=True, blank=True)
    image= models.TextField(null = True, blank=True)
    genre= models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    physical= models.BooleanField(default=False)
    artist = models.ForeignKey(ArtistOrBand, on_delete=models.SET_NULL, null=True)
    stock= models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    rating=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    priceP= models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    priceV= models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    bought= models.BooleanField(default=False)
    _id = models.AutoField(primary_key=True, editable=False)
    codeV = models.CharField(max_length=200, null=True, blank=True, default = random_string)
    codeP = models.CharField(max_length=200, null=True, blank=True, default = random_string)
    type= models.CharField(max_length=200, null=True, blank=True, default = "Album")

    #Constructor to display the name title
    def __str__(self):
        return str(self.title)

class Song(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    duration = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    file = models.FileField(upload_to='statics/', default="Some String")
    review = models.FileField(upload_to='statics/', default="Some String")
    price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    bought = models.BooleanField(default=False)
    image =  models.TextField(null = True, blank=True, default='bla')
    type= models.CharField(max_length=200, null=True, blank=True, default = "Song")

    #Constructor to display the song title
    def __str__(self):
        return str(self.title)


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    songs = models.ManyToManyField(Song, through='SongsPlaylist')
    name = models.CharField(max_length=200, null=True, blank=True)

    #Constructor to display the Playlist name
    def __str__(self):
        return str(self.name)

class Review(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    comment = models.TextField(null = True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    #Constructor to display the rating
    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    payMethod = models.CharField(max_length=200, null=True, blank=True)
    taxes = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    shiping = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    total = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    isPaid = models.BooleanField(default=False)
    paidAt =  models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 

    #Constructor to display the rating
    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)    
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True)
    qty = models.IntegerField(null = True, blank=True, default=0)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    image = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    #Constructor to display the order name
    def __str__(self):
        return str(self.name)

class ShippingAdress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    _id = models.AutoField(primary_key=True, editable=False)
    
    #Constructor to display the address
    def __str__(self):
        return str(self.address)



class SongsPlaylist(models.Model):
	song = models.ForeignKey(Song, related_name='SongsWithPlaylists', on_delete=models.DO_NOTHING)
	playlist = models.ForeignKey(Playlist, related_name='PlaylistsWithSongs', on_delete=models.DO_NOTHING)

	def __str__(self):
		return str(self.playlist)