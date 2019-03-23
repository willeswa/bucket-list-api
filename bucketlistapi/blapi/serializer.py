""" This module data serializer classes"""
from rest_framework import serializers
from .models import BucketList


class BucketListSerializer(serializers.ModelSerializer):
    """ Maps the model instance to JSON """

    class Meta:
        """ Maps serializer fields with the models fields """

        model = BucketList
        fields = ('id', 'name', 'created_on', 'modified_on')
        read_only_fields = ('created_on', 'modified_on')
