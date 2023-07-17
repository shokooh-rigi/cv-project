from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from cv_app.models import User, EducationHistory
from cv_app.serializers import (UserSerializer)
from cv_app.test.factories import EducationHistoryFactory, CertificateFactory


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

    # TODO: CREATE API USER VIEWS.PY
    def test_user_get(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('user_retrieve_update_destroy_api', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserSerializer(self.user).data)


class EducationHistoryTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'testuser', 'password': 'testpassword'}
        self.user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)
        self.education_obj = EducationHistoryFactory()
        self.education_url = reverse('cv_app:educations')

    def test_education_list(self):
        response = self.client.get(reverse(self.education_url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_education_create(self):
        new_education_obj = EducationHistoryFactory(major='software engineering', institution='sharif')
        response = self.client.post(reverse(self.education_url), new_education_obj)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CertificateTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'testuser', 'password': 'testpassword'}
        self.user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)
        self.certificate_obj = CertificateFactory()
        self.certificate_url = reverse('cv_app:certificates')

    def test_certificate_list(self):
        response = self.client.get(reverse(self.certificate_url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_certificate_create(self):
        new_certificate_obj = CertificateFactory(name='LPIC1', course_duration='6 month')
        response = self.client.post(reverse(self.certificate_url), new_certificate_obj)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)