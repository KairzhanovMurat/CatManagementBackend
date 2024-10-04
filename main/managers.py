from django.db import models


class CatManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(average_rating=models.Avg('cat_rates__rate', default=0))
