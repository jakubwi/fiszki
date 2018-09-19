from django.contrib import admin
from . import models
from .models import Deck

class CardInline(admin.TabularInline):
    model = models.Card

class DeckAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'slug' )
    inlines = [CardInline]
    prepopulated_fields = {'slug': ('name',)}

class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'deck')

admin.site.register(models.Deck, DeckAdmin)
admin.site.register(models.Card, CardAdmin)