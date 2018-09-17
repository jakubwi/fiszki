from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

class DeckListView(LoginRequiredMixin, ListView):
    model = models.Deck
    template_name = 'deck_list.html'
    login_url = 'login'

class DeckDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Deck
    template_name = 'deck_delete.html'
    success_url = reverse_lazy('deck_list')
    login_url = 'login'

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