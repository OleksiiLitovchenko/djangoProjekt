from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    slug = models.CharField(max_length=50, unique=True, db_index=True)
    photo = models.ImageField(upload_to='portfolioitem/')

class About(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='about/')
    descr = models.TextField(max_length=2000)


