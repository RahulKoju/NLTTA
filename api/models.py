from django.db import models

# Create your models here.

class Feed(models.Model):
    language = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    name_nepali = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255)
    website = models.URLField()
    logo_url = models.URLField()

    def __str__(self):
        return self.name # prints name if obj is printed


class FeedItem(models.Model):
    uuid = models.CharField(max_length=36, unique=True)
    slug = models.SlugField(unique=True, max_length=255)
    link = models.URLField()
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    image_url = models.URLField()
    
    published_at = models.DateTimeField()
    published_raw_nepali_date = models.CharField(max_length=50)
    fetched_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.title
