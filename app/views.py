import json
from typing import Generic
from .serializers import RegistrationSerializer, CategorySerializer, ContentSerializer
from django.contrib.auth import authenticate
from .models import CustomUser, Content, Category
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListCreateAPIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import filters
# Create your views here.



#Class based view to register/create user
class RegisterUserAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

# login view

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email=request.data.get('email')
    password=request.data.get('password')

    if email is None or password is None:
      return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
    user = authenticate(email=email, password=password)
    print(user)

    if not user:
          return Response({'error': 'Invalid Credentials'},
                          status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'id': token.user_id},
                    status=HTTP_200_OK)
                    
# to create the category

class CreateCategory(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# to create the content
class ContentCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

# list the content for particular user from the token which is passes in http header
def listContent(request):
    token=request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
    user=Token.objects.get(key=token).user_id
    content=Content.objects.filter(author=user)
    serializer=ContentSerializer(content, many=True)
    return JsonResponse(serializer.data, safe=False)

# list the content for Admin user from the token which is passes in http header
class AdminListContent(ListAPIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

# to update the content and all its aspect for admin user
class AdminRetriveContentUpdate(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
  
# to update the content and all its aspect for author user
class updateContent(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContentSerializer

    def get_queryset(self):
        token=self.request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user=Token.objects.get(key=token).user_id
        return Content.objects.filter(author=user)
    
# to delete the content for admin user
class AdminDeleteContent(DestroyAPIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

# to delete the content for author user
class AuthorDeleteContent(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContentSerializer
    
    def get_queryset(self):
        token=self.request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user=Token.objects.get(key=token).user_id
        return Content.objects.filter(author=user)

# search the content
class QuestionsAPIView(ListCreateAPIView):
    search_fields = ['title', 'body', 'summary','categories__name', 'author__first_name', 'author__last_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
