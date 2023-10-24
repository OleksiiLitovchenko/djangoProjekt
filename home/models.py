from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    slug = models.CharField(max_length=50, unique=True, db_index=True)
    photo = models.ImageField(upload_to='portfolioItem')

class About(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='portfolioItem')
    descr = models.TextField(max_length= 2000)

class Services(models.Model):
    class IconBox(models.Model):
        icon_class = models.CharField(max_length=50)
        title = models.CharField(max_length=100)
        description = models.TextField()
        is_visible = models.BooleanField()

        def __str__(self):
            return self.title

class Team(models.Model):
    class Chef(models.Model):
        name = models.CharField(max_length=100)
        slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
        position = models.CharField(max_length=100)

        bio = models.TextField()
        image = models.ImageField(upload_to='team/')
        twitter = models.URLField(blank=True)
        facebook = models.URLField(blank=True)
        instagram = models.URLField(blank=True)
        linkedin = models.URLField(blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        order = models.PositiveSmallIntegerField(unique=True)
        is_visible = models.BooleanField(default=True)

        def __str__(self):
            return self.name

        def get_social_links(self):
            social_links = {
                'twitter': self.twitter,
                'facebook': self.facebook,
                'instagram': self.instagram,
                'linkedin': self.linkedin,
            }
            return {platform: link for platform, link in social_links.items() if link}