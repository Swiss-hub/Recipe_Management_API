from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer, UserSerializer
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()
# -------------------
# Category ViewSet
# -------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# -------------------
# Recipe ViewSet
# -------------------
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        # Users can see all recipes
        return Recipe.objects.all()
    
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [] # Allow anyone to register