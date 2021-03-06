from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import SignUpForm, ContactForm
from .models import SignUp


def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # obj.full_name = obj.full_name or request.user or 'AnonymousUser'
        obj.save()
    context = {'title': 'Sign Up Now', 'form': form}
    if request.user.is_staff:
        context.update({'queryset': SignUp.objects.all().order_by('-added')})
    return render(request, 'home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        message = 'Hi {},\n\nThis is a test response to your question:'\
            '\n\n{}\n\nSent via {}.'.format(
                form.cleaned_data.get('full_name'),
                form.cleaned_data.get('message'),
                form.cleaned_data.get('email')
            )
        send_mail(
            'Contact form test response',
            message,
            settings.EMAIL_HOST_USER,
            [form.cleaned_data.get('email')],
            fail_silently=False
        )
    context = {'form': form}
    return render(request, 'contact.html', context)
