from django.db import models

class SiteUsers(models.Model):
    email = models.EmailField()
    dateOfBirth = models.DateTimeField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Item(models.Model):
    title = models.TextField()
    description = models.TextField()
    picture = models.ImageField(upload_to='images/')
    endDate = models.DateTimeField()
