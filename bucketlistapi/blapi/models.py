""" This module defines models """

from django.db import models

# Create your models here.


class BucketList(models.Model):
    """ Defines the structure for a Bucketlist object """

    name = models.CharField(max_length=65, blank=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Returns a rep of the model """
        return '{}'.format(self.name)
