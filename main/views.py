from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from . import serializers, filters, examples
from .models import Cat, Breed
from .permissions import IsOwnerOrReadOnly


class BaseOwnerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@extend_schema_view(
    list=extend_schema(
        summary="Список всех кошек",
        description="Получение списка всех кошек.",
        tags=['Кошки'],
        examples=examples.example_cat_list

    ),
    retrieve=extend_schema(
        summary="Получение кошки",
        description="Получение информации о конкретной кошке.",
        tags=['Кошки'],
        examples=[examples.example_cat_detail]
    ),
    create=extend_schema(
        summary="Создание новой кошки",
        description="Создание новой кошки с привязкой к породам.",
        tags=['Кошки'],
        examples=[examples.example_cat_create]
    ),
    update=extend_schema(
        summary="Обновление кошки",
        description="Обновление данных о кошке(доступно только владельцу).",
        tags=['Кошки'],
        examples=[examples.example_cat_create]
    ),
    partial_update=extend_schema(
        summary="Частичное обновление кошки",
        description="Частичное обновление информации о кошке(доступно только владельцу).",
        tags=['Кошки'],
        examples=[examples.example_cat_create]
    ),
    destroy=extend_schema(
        summary="Удаление кошки",
        description="Удаление кошки из базы данных(доступно только владельцу).",
        tags=['Кошки']
    )
)
class CatViewSet(BaseOwnerViewSet):
    queryset = Cat.objects.select_related('owner').prefetch_related('breeds').all()
    filterset_class = filters.CatFilter
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.CatDetailSerializer
        elif self.action == 'list':
            return serializers.CatListSerializer
        return serializers.CatWriteSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Список всех пород",
        description="Получение списка всех пород.",
        tags=['Породы'],
        examples=examples.example_breed_list
    ),
    retrieve=extend_schema(
        summary="Получение породы",
        description="Получение информации о конкретной породе.",
        tags=['Породы'],
        examples=[examples.example_breed_detail]
    ),
    create=extend_schema(
        summary="Создание новой породы",
        description="Создание новой породы с привязкой к владельцу.",
        tags=['Породы'],
        examples=[examples.example_breed_create]
    ),
    update=extend_schema(
        summary="Обновление породы",
        description="Обновление данных о породе(доступно только владельцу).",
        tags=['Породы'],
        examples=[examples.example_breed_create]
    ),
    partial_update=extend_schema(
        summary="Частичное обновление породы",
        description="Частичное обновление информации о породе(доступно только владельцу).",
        tags=['Породы'],
        examples=[examples.example_breed_create]

    ),
    destroy=extend_schema(
        summary="Удаление породы",
        description="Удаление породы из базы данных(доступно только владельцу).",
        tags=['Породы']
    )
)
class BreedViewSet(BaseOwnerViewSet):
    queryset = Breed.objects.select_related('owner').all()
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.BreedDetailSerializer
        elif self.action == 'list':
            return serializers.BreedListSerializer
        return serializers.BreedWriteSerializer


@extend_schema_view(
    post=extend_schema(
        summary="Оценить кошку",
        description="Добавление оценки для конкретной кошки.",
        tags=['Оценки кошек'],
        examples=[examples.example_cat_rate]
    )
)
class CatRateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CatRateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

