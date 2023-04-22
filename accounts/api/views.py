from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from ..models import MyUser
from .serializers import MyUserSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = MyUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "User Created Succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['age'] = user.age
        token['skin_tone'] = user.skin_tone
        token['body_shape'] = user.body_shape
        token['mobile_number'] = user.mobile_number
        token['gender'] = user.gender
        try:
            token['avatar'] = user.avatar.url
            token['profile_picture'] = user.profile_picture.url
        except:
            token['avatar'] = None
            token['profile_picture'] = None

        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/user',
        'api/user/refresh',
        'api/user/create',
    ]

    return Response(routes)
