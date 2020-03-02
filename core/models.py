from django.db import models


class TimeStapedModel(models.Model):

    """ Time Staped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
