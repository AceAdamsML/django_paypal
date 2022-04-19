from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image_url= models.ImageField(max_length=1000, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    booked_seats = models.ManyToManyField('Seat', blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    movie = models.ForeignKey(Movie, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie.name


class Seat(models.Model):
    seat_no=models.IntegerField()
    occupant_first_name=models.CharField(max_length=255)
    occupant_last_name=models.CharField(max_length=255)
    occupant_email=models.EmailField(max_length=555)
    purchase_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.occupant_first_name}-{self.occupant_last_name} seat_no {self.seat_no}"
