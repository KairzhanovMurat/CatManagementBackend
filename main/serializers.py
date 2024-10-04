from django.db import transaction
from rest_framework import serializers

from . import models
from .models import Breed


class BaseBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Breed
        fields = ['id', 'name']
        read_only_fields = ['id']
        ordering = ['id', 'name']


class BreedListSerializer(BaseBreedSerializer):
    """
    Схема получения списка пород
    """
    owner = serializers.StringRelatedField(read_only=True)

    class Meta(BaseBreedSerializer.Meta):
        fields = BaseBreedSerializer.Meta.fields + ['owner']


class BreedDetailSerializer(BreedListSerializer):
    """
    Схема получения подробной информации о породе
    """

    class Meta(BreedListSerializer.Meta):
        fields = BreedListSerializer.Meta.fields + ['description']


class BreedWriteSerializer(BaseBreedSerializer):
    """
    Схема создания/редактирования информации о породе
    """

    class Meta(BaseBreedSerializer.Meta):
        fields = BaseBreedSerializer.Meta.fields + ['description']


class BaseCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cat
        fields = ['id', 'name', 'age', 'color']
        read_only_fields = ['id']
        ordering = ['id', 'name', 'age', 'color']


class CatListSerializer(BaseCatSerializer):
    """
    Схема получения списка кошек
    """
    owner = serializers.StringRelatedField(read_only=True)
    breeds = serializers.StringRelatedField(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.average_rating

    class Meta(BaseCatSerializer.Meta):
        fields = BaseCatSerializer.Meta.fields + ['owner', 'breeds', 'average_rating']


class CatDetailSerializer(CatListSerializer):
    """
    Схема получения подробной информации о кошке
    """

    class Meta(CatListSerializer.Meta):
        fields = CatListSerializer.Meta.fields + ['description']


class CatWriteSerializer(BaseCatSerializer):
    """
    Схема создания/редактирования информации о кошке
    """
    breeds = BreedWriteSerializer(many=True, required=False)

    class Meta(BaseCatSerializer.Meta):
        fields = BaseCatSerializer.Meta.fields + ['breeds', 'description']

    def _create_breeds(self, cat, breeds_data):
        user = self.context['request'].user
        for breed in breeds_data:
            breed, created = Breed.objects.get_or_create(**breed)
            if created:
                breed.owner = user
                breed.save()

            cat.breeds.add(breed)

    @transaction.atomic
    def create(self, validated_data):
        breeds_data = validated_data.pop('breeds', [])
        cat = models.Cat.objects.create(**validated_data)
        self._create_breeds(cat, breeds_data)
        return cat

    @transaction.atomic
    def update(self, instance, validated_data):
        breeds_data = validated_data.pop('breeds', None)
        if breeds_data:
            instance.breeds.clear()
            self._create_breeds(instance, breeds_data)
        return super().update(instance, validated_data)


class CatRateSerializer(serializers.ModelSerializer):
    """
    Схема создания оценки кошки
    """

    class Meta:
        model = models.CatRate
        exclude = ['user']
