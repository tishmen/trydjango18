from django.shortcuts import render

# Create your views here.


def home(request):
    title = 'Welcome!'
    if request.user.is_authenticated():
        title = 'Welcome! {}'.format(request.user)
    context = {'title': title}
    return render(request, 'home.html', context)
