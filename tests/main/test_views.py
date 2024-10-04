import pytest
from django.urls import reverse
from rest_framework import status
from ..factories import CatFactory, BreedFactory, CatRateFactory

@pytest.mark.django_db
class TestBreedViews:
    def test_breed_list(self, auth_client):
        # Create some breeds
        BreedFactory.create_batch(5)

        # Test the breed list endpoint
        response = auth_client.get(reverse('breeds-list'))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 5

    def test_create_breed(self, auth_client):
        data = {
            'name': 'Persian',
            'description': 'Fluffy and cute.'
        }

        response = auth_client.post(reverse('breeds-list'), data=data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['name'] == 'Persian'


@pytest.mark.django_db
class TestCatViews:
    def test_create_cat(self, auth_client):
        breed = BreedFactory()
        data = {
            'name': 'Whiskers',
            'age': 24,
            'color': 'White',
            'description': 'Friendly cat',
            'breeds': [{'id': breed.id, 'name': breed.name}],
        }

        response = auth_client.post(reverse('cats-list'), data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_cat_list(self, auth_client):
        # Create some cats
        CatFactory.create_batch(3)

        response = auth_client.get(reverse('cats-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 3

    # def test_rate_cat(self, auth_client):
    #     cat = CatFactory()
    #
    #     data = {'rate': 5}
    #     response = auth_client.post(reverse('rate'), data=data, format='json')
    #     assert response.status_code == status.HTTP_201_CREATED
    #     assert cat.cat_rates.count() == 1
    #     assert cat.cat_rates.first().rate == 5
