from rest_framework import serializers 
from .models import User
from django.db import transaction

class registerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField()
    first_name = serializers.CharField(required=True , max_length=150)
    last_name = serializers.CharField(required=True , max_length=150)

    class Meta:
        model = User
        fields = ['username','phone_number', 'email', 'password', 'confirm_password', 'first_name', 'last_name']
    
    """ this method is used to validate the password and confirm password """

    def validate(self, data):
        if data['password' ] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    """ this method is used to validate the phone number """
    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Phone number already in use")
        return value
            
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            return user

