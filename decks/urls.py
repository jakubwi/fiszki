from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.DeckListView.as_view(), name='deck_list'),
    path('<slug:slug>/delete/', views.DeckDeleteView.as_view(), name='deck_delete'),
    path('new/', views.DeckCreateView.as_view(), name='deck_new'),
#    path('<slug:slug>/cards/new/', views.CardCreateView.as_view(), name='card_new'),
    path('<slug:slug>/cards/new/', views.CardCreateView, name='card_new'),
    path('cards/<pk>/delete/', views.CardDeleteView.as_view(), name='card_delete'),
    path('<slug:slug>/learning/', views.LearningView, name='learning'),
]
