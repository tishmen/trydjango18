from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SignUp(models.Model):

    # extend models beyond what's in coursework

    email = models.EmailField()
    full_name = models.CharField(max_length=100, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.email
