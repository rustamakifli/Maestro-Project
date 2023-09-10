from django.urls import path, include
from core.api import views
urlpatterns = [
    path('blogs/', views.BlogListView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('orders/', views.OrderListView.as_view()),
]