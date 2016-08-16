from django import forms

from .models import SignUp


class ContactForm(forms.Form):

    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    # use textarea widget for message
    message = forms.CharField()


class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        # raise ValidationError on all temporary email addresses
        # domain list https://gist.github.com/adamloving/4401361
        email = self.cleaned_data.get('email')
        local, domain = email.split('@')
        if '.edu' not in domain:
            raise forms.ValidationError('Please use .edu email address')
        return email
