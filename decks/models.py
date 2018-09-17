from django.db import models
from django.conf import settings
from django.urls import reverse

class Deck(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('deck_detail', args=[str(self.id)])

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')
    name = models.CharField(max_length=255)
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.id)])