from rest_framework import serializers
from core.models import (Blog,Order,Service,Pros)
from users.api.serializers import UserDetail


class BlogListSerializer(serializers.ModelSerializer):
    author = UserDetail()
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'description', 'image', 'is_active', 'createdAt']

class BlogDetailSerializer(serializers.ModelSerializer):
    author = UserDetail()
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'description', 'image', 'is_active', 'createdAt']

class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields = ['id', 'title', 'description', 'image']

class ProSerializer(serializers.ModelSerializer):
    user = UserDetail()
    class Meta:
        model=Pros
        fields = ['id', 'user', 'address', 'bio', 'image', 'completedtasks','createdAt']


class OrderListSerializer(serializers.ModelSerializer):
    subService = SubServiceSerializer()
    pro = ProSerializer()
    class Meta:
        model=Order
        fields = ['id', 'pro', 'service', 'startDate', 'address', 'status', 'createdAt', 'totalAmount']

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = ['id', 'customer', 'pro','service', 'startDate', 'address', 'status', 'createdAt', 'detail', 'totalAmount', ]