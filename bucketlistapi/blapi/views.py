""" This module definnes the app views """
from rest_framework import generics
from .serializer import BucketListSerializer
from .models import BucketList

# Create your views here.
class  CreateView(generics.ListCreateAPIView):
    """ This class defines the create view """
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def create_bucket(self, serializer):
        """ Serializer for creating the bucketlist """
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Defines the GET, UPDATE and DELETE functionality """
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    
