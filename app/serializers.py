from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser, Category, Content
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import password_validation
from django.contrib.auth import authenticate
from rest_framework.fields import CurrentUserDefault


class RegistrationSerializer(serializers.ModelSerializer):

    # fields validations
    email=serializers.EmailField(validators=[UniqueValidator(queryset=CustomUser.objects.all())], required=True)
    address=serializers.CharField(allow_blank=True,allow_null=True)
    Phone=serializers.CharField(min_length=10, max_length=10)
    city=serializers.CharField(allow_blank=True,allow_null=True)
    state=serializers.CharField(allow_blank=True,allow_null=True)
    country=serializers.CharField(allow_blank=True,allow_null=True)
    pincode=serializers.CharField(min_length=6, max_length=6)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password], style={'input_type': 'password'}, allow_blank=False)

    # to create
    def create(self, validated_data):
            user = CustomUser.objects.create(
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                address=validated_data['address'],
                Phone=validated_data['Phone'],
                city=validated_data['city'],
                state=validated_data['state'],
                country=validated_data['country'],
                pincode=validated_data['pincode'],
            )
            user.set_password(validated_data['password']) 
            print(user.set_password(validated_data['password']))
            user.save()
            return user

    def update(self, instance, validated_data):
            user = super().update(instance, validated_data)
            if 'password' in validated_data:
                user.set_password(validated_data['password'])
                user.save()
            return user


    class Meta:
        model=CustomUser

        fields=['email', 'password', 'first_name', 'last_name', 'Phone', 'address', 'city', 'state', 'country', 'pincode']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name']

class ContentSerializer(serializers.ModelSerializer):


    categories=serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all().filter(user_type='AUTHOR'), default=CurrentUserDefault())
    document=serializers.FileField(use_url =True)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.body = validated_data['body']
        instance.summary = validated_data['summary']
        instance.document = validated_data['document']
        instance.save()

        return instance

    class Meta:
        model=Content
        fields= ['title', 'body', 'summary', 'document', 'categories', 'author']

        
