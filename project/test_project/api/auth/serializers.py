from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    """
    Registration serializer for requests and user creation
    """
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email','username', 'first_name', 'last_name','password', 'tg_user_name', 'tg_id', 'tg_first_name', 'tg_last_name']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
