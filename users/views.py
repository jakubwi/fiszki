import json
import urllib
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .forms import CustomUserCreationForm, CustomUserChangeForm
from . import models
from .models import CustomUser
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class ActivationConfirmView(TemplateView):
    template_name = 'acc_active_confirm.html'

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = models.CustomUser
    template_name = 'user_delete.html'
    success_url = reverse_lazy('about')
    login_url = 'login'
    success_message = "Your account has been successfully deleted. We are sorry to see you go!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UserDeleteView, self).delete(request, *args, **kwargs)
 
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            ### Begin reCAPTCHA validation ###
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ### End reCAPTCHA validation ###

            if result['success']:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                send_account_activation_email(request, user)
                return redirect('activation_confirm')
            else:
                messages.error(request, 'Are you really a robot? Please try again.')
                
            return redirect('signup')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def send_account_activation_email(request, CustomUser):
    text_content = 'Account Activation Email'
    subject = 'Email Activation'
    template_name = "acc_active_email.html"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipients = [CustomUser.email]
    kwargs = {
        "uidb64": urlsafe_base64_encode(force_bytes(CustomUser.pk)).decode(),
        "token": default_token_generator.make_token(CustomUser)
    }
    activation_url = reverse("activate_user_account", kwargs=kwargs)

    activate_url = "{0}://{1}{2}".format(request.scheme, request.get_host(), activation_url)

    context = {
        'CustomUser': CustomUser,
        'activate_url': activate_url
    }
    html_content = render_to_string(template_name, context)
    email = EmailMultiAlternatives(subject, text_content, from_email, recipients)
    email.attach_alternative(html_content, "text/html")
    email.send()

class ActivationCompleteView(TemplateView):
    template_name = 'acc_active_complete.html'

def activate_user_account(request, uidb64=None, token=None):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except CustomUser.DoesNotExist:
        user = None
    if user and default_token_generator.check_token(user, token):
        user.is_email_verified = True
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('activation_complete')
    else:
        return HttpResponse("Activation link has expired")