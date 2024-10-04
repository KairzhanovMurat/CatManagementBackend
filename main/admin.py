from django.contrib import admin

from .models import Cat, Breed, CatRate


class CatRateInline(admin.TabularInline):
    model = CatRate
    extra = 1


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    search_fields = ['name', 'owner', 'description', 'age', 'color']
    sortable_by = ['name', 'age', 'color']
    inlines = [CatRateInline]


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
