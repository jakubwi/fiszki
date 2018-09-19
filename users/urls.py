from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ActivationCompleteView.as_view(), name='activation_complete'),
    path('confirm/', views.ActivationConfirmView.as_view(), name='activation_confirm'),
    path('signup/', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_user_account, name='activate_user_account'),
]