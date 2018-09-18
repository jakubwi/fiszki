from django.db import models
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify

class Deck(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Deck, self) .save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('deck_list')

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.id)])