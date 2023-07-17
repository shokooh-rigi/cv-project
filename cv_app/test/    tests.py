from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from cv_app.models import User, EducationHistory
from cv_app.serializers import (UserSerializer)


class UserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'testuser', 'password': 'testpassword'}
        self.user = User.objects.create_user(**self.user_data)

    def test_user_create(self):
        response = self.client.post(reverse('user_create_api'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    # TODO: CREATE API USER VIEWS.PY
    def test_user_get(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('user_retrieve_update_destroy_api', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserSerializer(self.user).data)


class EducationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'testuser', 'password': 'testpassword'}
        self.user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)
        # TODO: add factory education and use it here
        self.education_data = {'user': self.user.id, 'institution': 'Test University', 'degree': 'Test Degree',
                              'field_of_study': 'Test Field', 'start_date': '2020-01-01', 'end_date': '2022-01-01'}
        self.education = EducationHistory.objects.create(**self.education_data)

    def test_education_list(self):
        response = self.client.get(reverse('education_list_create_api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_education_create(self):
        new_education_data = {'user': self.user.id, 'institution': 'New University', 'degree': 'New Degree',
                              'field_of_study': 'New Field', 'start_date': '2022-01-01', 'end_date': '2024-01-01'}
        response = self.client.post(reverse('education_list_create_api'), new_education_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EducationHistory.objects.count(), 2)
