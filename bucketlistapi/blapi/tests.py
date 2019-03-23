""" This module contains the test suit """

from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from .models import BucketList

# Create your tests here.


class ModelTestCase(TestCase):
    """ Defines the test suit for the models """

    def setUp(self):
        """ Defines test variables """

        self.client = APIClient()
        self.sample_bl = {'name': 'Eat an orange on Mt. Everest'}
        self.response = self.client.post(
            reverse("create"),
            self.sample_bl,
            format="json"
        )
        self.bl_name = "Become a worldclass software engineer"
        self.buckelist = BucketList(name=self.bl_name)

    def test_create_bucket_list_model(self):
        """ Tests the model method for creating a bucket list  """

        old_count = BucketList.objects.count()
        self.buckelist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_view_can_post(self):
        """ Tests if the view can post bucketlist data """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_a_bucketlist(self):
        """ Test if one can get a single bucket list """

        bucketlist = BucketList.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': bucketlist.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)
