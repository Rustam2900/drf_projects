from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('profile/', views.ProfileApiView.as_view(), name='profile'),
    path('category-list/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('post-list/', views.PostListAPIView.as_view(), name='post-list'),
    path('post-create/', views.PostListCreateAPIView.as_view(), name='post-create'),
    path('post-update/<int:pk>/', views.UpdatePostAPIView.as_view(), name='post-update'),
    path('category-create/', views.CategoryListCreateAPIView.as_view(), name='category-create'),
    path('category-update/<int:pk>/', views.CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category-delet/<int:pk>/', views.CategoryDestroyAPIView.as_view(), name='category-destroy'),
]
