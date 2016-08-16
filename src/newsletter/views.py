from django.shortcuts import render

from .forms import SignUpForm, ContactForm

# Create your views here.


def home(request):
    title = 'Hello'
    if request.user.is_authenticated():
        title += ' {}'.format(request.user)
    form = SignUpForm(request.POST or None)
    context = {'title': title, 'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        if not obj.full_name:
            obj.full_name = 'default'
        obj.save()
    return render(request, 'home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for k, v in form.cleaned_data.iteritems():
            print(k, v)
        # full_name = form.cleaned_data.get('full_name')
        # email = form.cleaned_data.get('email')
        # message = form.cleaned_data.get('message')
        # print(full_name, email, message)
    context = {'form': form}
    return render(request, 'contact.html', context)
