from django.db import models
from django.contrib.auth.models import User


class SiteUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateOfBirth = models.DateField()

    def __str__(self):
        return self.user.username


class Item(models.Model):
    title = models.TextField()
    description = models.TextField()
    picture = models.ImageField(upload_to='images/')
    endDate = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.TextField()

    def __str__(self):
        return self.title

class Bid(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(SiteUsers, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
