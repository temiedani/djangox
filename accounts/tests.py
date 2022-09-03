from django.test import TestCase
from .models import CustomUser
from .views import RegisterAPI
from django.urls import reverse, resolve
from .views import RegisterAPI, getRoutes, getUsers
from .serializers import RegisterSerializer, UserSerializer


# test model.py

class TestModels(TestCase):

    # test the string method in model.py
    def test_model_str(self):
        testUser = CustomUser.objects.create(
            username="test", email="test@company.com")
        self.assertEqual(str(testUser), "test@company.com")


class TestViews(TestCase):

    # Test staff user creation:
    # def test_create_user(self):
    #     testUser = CustomUser.objects.create(
    #         username="test", email="test@company.com", password="@1TestPassword")
    #     serializer = RegisterSerializer(testUser, many=False)

    #     created_user = RegisterSerializer.create(testUser)
    #     self.assertEqual(testUser.is_staff, "true")
    pass


class TestSerializer(TestCase):
    pass


class TestUrls(TestCase):
    def test_createUser_url_is_resolved(self):
        url = reverse('createUser')
        self.assertEquals(resolve(url).func.view_class, RegisterAPI)

    # def test_getUsers_url_is_resolved(self):
    #     url = reverse('getUsers')
    #     self.assertEquals(resolve(url).func.view_class, getUsers)
