import json
import uuid

from django.test import Client, TestCase
from app.docs import ProfileDocType
from app.models import Activation


class APITest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        ProfileDocType.reset()

        activation = Activation.objects.create(name='Test Activation')

        cls.profile1 = ProfileDocType(
            meta={'id': str(uuid.uuid4())},
            brand_ids=[1, 2],
        )
        cls.profile1.save()

        cls.profile2 = ProfileDocType(
            meta={'id': str(uuid.uuid4())},
            brand_ids=[],
        )
        cls.profile2.save()

        activation.submissions.create(profile_id=cls.profile1._id)
        activation.submissions.create(profile_id=cls.profile2._id)

        ProfileDocType.flush()

    def setUp(self):
        self.client = Client()

    def test_activation_list(self):
        response = self.client.get('/activations')
        activations = json.loads(response.content)

        self.assertEqual(len(activations), 1)
        self.assertEqual(activations[0]['name'], 'Test Activation')

    def test_profile_list(self):
        response = self.client.get('/profiles')
        profiles = json.loads(response.content)

        self.assertEqual(
            sorted([p['id'] for p in profiles]),
            sorted([self.profile1._id, self.profile2._id]),
        )
        self.assertEqual(
            sorted([p['brand_ids'] for p in profiles]),
            [[], [1, 2]],
        )
