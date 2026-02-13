from django.db import models
from ships.models import Ship

# Create your models here.

class Component(models.Model):
    ship = models.ForeignKey(Ship,on_delete=models.CASCADE,related_name='components')
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=30)
    installed_date = models.DateField()
    last_maintenance = models.DateField()

    def __str__(self):
        return f"{self.name} - ({self.ship.name})"