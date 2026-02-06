from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Franchise(models.Model):
    name= models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    founded_year = models.IntegerField()
    no_of_trophies = models.IntegerField()
    logo = models.ImageField(upload_to='ipl_logo/',blank=True,null=True)
    city = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    coach = models.CharField(max_length=50)

    class Meta:
        db_table = 'franchises'

    def __str__(self):
        return f"{self.name}({self.short_name})"
    

class Players(models.Model):
    role_choices=[
        ('Batsman','Batsman'),
        ('Bowler','Bowler'),
        ('Wicket-Keeper','Wicket-Keeper'),
        ('All-Rounder','All-Rounder'),
    ]
    name = models.CharField(max_length=50)
    age = models.PositiveBigIntegerField()
    role = models.CharField(max_length=50, choices = role_choices )
    nationality = models.CharField(max_length=50)
    franchise = models.ForeignKey(Franchise,on_delete= models.CASCADE)
    photo = models.ImageField(upload_to='players/',blank=True,null=True)

    def __str__(self):
        return f"{self.name} ({self.role})"
    

class Stadium(models.Model):
    name = models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    capacity = models.IntegerField()
    home_team = models.ForeignKey(Franchise,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=12,blank=True)
    address = models.CharField(max_length=100,blank=True)
    profile_photo = models.ImageField(upload_to='profile_pics/',blank=True,null=True)

    def __str__(self):
        return self.user.username