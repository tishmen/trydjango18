from django.shortcuts import render

from .forms import SignUpForm

# Create your views here.


def home(request):
    title = 'Welcome!'
    if request.user.is_authenticated():
        title += ' {}'.format(request.user)
    form = SignUpForm(request.POST or None)
    context = {'title': title, 'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        if not obj.full_name:
            obj.full_name = 'tishmen'
        obj.save()
        context = {'title': 'Thank you'}
    return render(request, 'home.html', context)
