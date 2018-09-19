from django.urls import path
from . import views

urlpatterns = [
    path('', views.AboutPageView.as_view(), name='about'),
    path('account/<username>/', views.AccountPageView.as_view(), name='user_account_page')
]