from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import serializers, examples


@extend_schema_view(
    post=extend_schema(
        summary="Получение jwt токена",
        description="Получение jwt токена при предоставлении емейла и пароля.",
        tags=['Пользователи'],
    )
)
class TokenView(TokenObtainPairView):
    pass


@extend_schema_view(
    post=extend_schema(
        summary="Получение refresh токена",
        description="Получение jwt токена при предоставлении refresh токена.",
        tags=['Пользователи'],
    )
)
class RefreshView(TokenRefreshView):
    pass


@extend_schema_view(
    post=extend_schema(
        summary="Регистрация",
        description="создание нового пользовтаеля в системе.",
        tags=['Пользователи'],
        examples=[examples.example_user_create]
    )
)
class CreateUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.CreateUserSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Информация о текущем пользователе",
        description="Получение информации о текущем пользователе.",
        tags=['Пользователи'],
        examples=[examples.example_user]
    ),
    put=extend_schema(
        summary="Обновление",
        description="Обновление текущего пользователя.",
        tags=['Пользователи'],
        examples=[examples.example_user]
    ),
    patch=extend_schema(
        summary="Частичное обновление",
        description="Частичное обновление текущего пользователя.",
        tags=['Пользователи'],
        examples=[examples.example_user]
    ),
    delete=extend_schema(
        summary="Удаление",
        description="Удаление текущего пользователя.",
        tags=['Пользователи']
    )
)
class ManageCurrentUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CreateUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
