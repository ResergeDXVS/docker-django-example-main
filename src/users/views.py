from django.shortcuts import render
from .forms import UserForm

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def userCreate(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("Usuario registrado")
    return render(request, "users/user_form.html",context={"form":form})


class APIUser(ViewSet):
    user_serializer = UserSerializer

    def list(self, request):
        """Listado de usuarios registrados"""
        users = User.objects.all()
        serializer = self.user_serializer(users, many=True)
        return Response({
            "list_users": serializer.data
        })
    
    def create(self, request):
        """Crear un nuevo usuario"""
        serializer = self.user_serializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(**serializer.validated_data)
            user_data = self.user_serializer(user).data
            return Response({
                "message": f"Usuario creado con ID {user.id}",
                "data": user_data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Consulta de un usuario por su id"""
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.user_serializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Actualización completa de un usuario"""
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.user_serializer(user, data=request.data)
        if serializer.is_valid():
            for attr, value in serializer.validated_data.items():
                setattr(user, attr, value)
            user.save()
            return Response(self.user_serializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """Actualización parcial de un usuario"""
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.user_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            for attr, value in serializer.validated_data.items():
                setattr(user, attr, value)
            user.save()
            return Response(self.user_serializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Eliminación de un usuario"""
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"message": f"Usuario con ID {pk} eliminado"}, status=status.HTTP_204_NO_CONTENT)






class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Devuelve los datos del usuario autenticado (requiere JWT válido)"""
        if not request.user or not request.user.is_authenticated:
            return Response(
                {"error": "No autenticado"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return []
