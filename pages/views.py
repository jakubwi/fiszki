from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class AboutPageView(TemplateView):
    template_name = 'about.html'

class AccountPageView(LoginRequiredMixin, TemplateView):
    template_name = 'user_account_page.html'