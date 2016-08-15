from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp

# Register your models here.


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):

    form = SignUpForm
    list_display = ['email', 'added', 'changed']
