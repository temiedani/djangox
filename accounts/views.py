
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

from .models import CustomUser
from .serializers import UserSerializer


# API Documentation page
# @api_view: decorator for working with function based views.
@api_view(['GET'])
def getRoutes(request):
    routes = {'Create New User': 'POST /api/createUser',
              'Get a list of all Users': 'GET /api/getUsers',
              'Get a User by ID': 'GET /api/getUsers/id',
              }
    return Response(routes)


# Register API
# APIView: class for working with class-based views.
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# List all Users
# @api_view: decorator for working with function based views.
@api_view(['GET'])
def getUsers(request):
    users = CustomUser.objects.order_by('-is_staff')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# List Users by ID
# @api_view: decorator for working with function based views.
@api_view(['GET'])
def getUser(request, pk):
    users = CustomUser.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)
