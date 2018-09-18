from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from .models import Card, Deck
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


class DeckListView(LoginRequiredMixin, ListView):
    model = models.Deck
    template_name = 'deck_list.html'
    login_url = 'login'
    paginate_by = 3

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

# CARD views

class CardCreateView(LoginRequiredMixin, CreateView):
    model = models.Card
    template_name = 'card_new.html'
    login_url = 'login'
    fields = ['deck', 'name', 'front', 'back']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Card
    template_name = 'card_delete.html'
    success_url = reverse_lazy('deck_list')
    login_url = 'login'

    def get_queryset(self):
        return Card.objects.filter(author=self.request.user)

@login_required
def LearningView(request, slug):
    deck = Deck.objects.get(slug=slug, author=request.user)
    card_list = Card.objects.filter(deck=deck, author=request.user)
    paginator = Paginator(card_list, 1)
    page = request.GET.get('page')
    context_dict = {}
    try: 
        deck = Deck.objects.get(slug=slug, author=request.user)
        cards = Card.objects.filter(deck=deck, author=request.user)
        cards = paginator.page(page)
        context_dict['cards'] = cards
        context_dict['deck'] = deck
    except PageNotAnInteger:
        cards = paginator.page(1)
    except EmptyPage:
        cards = paginator.page(paginator.num_pages)
    except Deck.DoesNotExist:
        context_dict['cards'] = None
        context_dict['deck'] = None

    return render(request, 'learning.html', {'cards': cards, 'deck': deck, 'page': page, })