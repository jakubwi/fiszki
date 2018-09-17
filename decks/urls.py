from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.DeckListView.as_view(), name='deck_list'),
    path('<int:pk>/detail/', views.DeckDetailView.as_view(), name='deck_detail'),
    path('<int:pk>/delete/', views.DeckDeleteView.as_view(), name='deck_delete'),
    path('new/', views.DeckCreateView.as_view(), name='deck_new'),
]