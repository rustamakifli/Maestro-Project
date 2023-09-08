from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.password_validation import validate_password
from rest_framework import status

User = get_user_model()

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'birth_date', 'image', 'gender']
        extra_kwargs = {
            "first_name": {'required': True},
            "last_name": {'required': True},
            "email": {'required': True},
            "password": {'required': True},
        }

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        user = super(MyUserSerializer, self).create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
    
class UserDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'image', 'gender','birth_date','date_joined']

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'image')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'image': {'required': False}
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You don't have permission for this user."})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.image = validated_data['image'] if 'image' in validated_data else instance.image
        instance.gender = validated_data['gender']
        instance.birth_date = validated_data['birth_date']
        instance.save()

        return instance