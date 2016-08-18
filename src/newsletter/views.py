from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import SignUpForm, ContactForm


def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.full_name = obj.full_name or request.user or 'AnonymousUser'
        obj.save()
    return render(request, 'home.html', {'title': 'Welcome', 'form': form})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for k, v in form.cleaned_data.iteritems():
        #     print(k, v)
        full_name = form.cleaned_data.get('full_name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        subject = 'this is subject'
        msg = '{}, {} via {}'.format(full_name, message, email)
        send_mail(
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
    context = {'form': form}
    return render(request, 'contact.html', context)
