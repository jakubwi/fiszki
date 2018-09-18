from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from .models import Card, Deck


class DeckListView(LoginRequiredMixin, ListView):
    model = models.Deck
    template_name = 'deck_list.html'
    login_url = 'login'

    def get_queryset(self):
        return Deck.objects.filter(author=self.request.user)

class DeckDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Deck
    template_name = 'deck_delete.html'
    success_url = reverse_lazy('deck_list')
    login_url = 'login'

    def get_queryset(self):
        return Deck.objects.filter(author=self.request.user)

class DeckCreateView(LoginRequiredMixin, CreateView):
    model = models.Deck
    template_name = 'deck_new.html'
    fields = ['name', 'description']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeckDetailView(LoginRequiredMixin, DetailView):
    model = models.Deck
    template_name = 'deck_detail.html'
    login_url = 'login'

    def get_queryset(self):
        return Deck.objects.filter(author=self.request.user)

# CARD views

class CardCreateView(LoginRequiredMixin, CreateView):
    model = models.Card
    template_name = 'card_new.html'
    login_url = 'login'
    fields = ['deck', 'name', 'front', 'back']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CardDetailView(LoginRequiredMixin, DetailView):
    model = models.Card
    template_name = 'card_detail.html'
    login_url = 'login'

    def get_queryset(self):
        return Card.objects.filter(author=self.request.user)

    def get_object(self):
        slug = self.kwargs['slug']
        pk2 = self.kwargs['pk2']
        deck = get_object_or_404(Deck, slug=slug)
        card = get_object_or_404(Card, pk=pk2)
        return card