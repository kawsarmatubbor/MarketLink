from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    password_2 = serializers.CharField(
        write_only = True,
        required = True
    )

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'profile_picture', 'password', 'password_2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_2']:
            raise serializers.ValidationError({
                "error" : "Passwords didn't match."
            })
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_2')
        user = CustomUser.objects.create_user(**validated_data)
        return user