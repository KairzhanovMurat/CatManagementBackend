import django_filters
from .models import Cat


class CatFilter(django_filters.FilterSet):
    breed = django_filters.CharFilter(field_name='breeds__name', lookup_expr='exact')
    age = django_filters.CharFilter(field_name='age', lookup_expr='exact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    color = django_filters.CharFilter(field_name='color', lookup_expr='icontains')


    class Meta:
        model = Cat
        fields = ['name', 'breed', 'color', 'age']
