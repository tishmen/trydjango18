from django.contrib import admin

from .models import SignUp

# Register your models here.


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):

    list_display = ['email', 'added', 'changed']
