from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.shortcuts import redirect
from .models import CustomUser
import re


# User Serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_staff', 'date_joined')
        # fields = '__all__'   #replace with this to get all user fields


def isStaffEmail(email):
    """A Helper function to check if an email is registered with company domain
    Args:
        email (string): user email
    Returns:
        _boolean_: true if staff email, false otherwise.
    """
    pattern = "[a-z.]*[@]company.com"
    # using regex check for users with email addresses if domain is @company.com
    if(re.search(pattern, email)):
        return True
    else:
        return False


# Register Serializer
class RegisterSerializer(ModelSerializer):

    # Serialize email and check if it is unique
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    # Serialize username and check if it is unique
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Function to create user object after POST request.
        Args:
            validated_data (dict): validated user data.
        Returns:
            _CustomUser_: returns json format of the created user.
        """
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'], validated_data['password'])
        # use the helper function isStaffEmail(email) to check if staff is user
        if(isStaffEmail(validated_data['email'])):
            # set as staff user
            user.is_staff = True
            user.save()
        return user
