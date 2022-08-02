# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from User.models import CustomUser
from User.serializers import UsersSerializer, CreateUserSerializer


class ListUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(is_active=True, is_staff=False)
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)


class CreateUserView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )
