from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from core.models import Blog,Order
from core.api.serializers import BlogListSerializer, BlogDetailSerializer,OrderListSerializer,OrderCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class BlogListView(ListAPIView):
    queryset = Blog.objects.filter(is_active = True)
    serializer_class = BlogListSerializer

class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer

class OrderListView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        orders = Order.objects.filter(customer=self.request.user)
        serializer = OrderListSerializer(orders, many=True)
        return Response({"orders": serializer.data})

    def post(self, request):
        order_data = request.data
        serializer = OrderCreateSerializer(data=order_data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": True}, status=status.HTTP_201_CREATED)

        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)