import pytest
from django.urls import reverse
from rest_framework import status

from ..factories import CatFactory, BreedFactory


@pytest.mark.django_db
class TestBreedViews:
    def test_breed_list(self, auth_client):
        BreedFactory.create_batch(5)

        response = auth_client.get(reverse('breeds-list'))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 5

    def test_create_breed(self, auth_client):
        data = {
            'name': 'Персидский',
            'description': 'Мягкий and пушистый.'
        }

        response = auth_client.post(reverse('breeds-list'), data=data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['name'] == 'Персидский'

    def test_create_breed_missing_name(self, auth_client):
        data = {
            'description': 'Мягкий и пушистый.'
        }

        response = auth_client.post(reverse('breeds-list'), data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'name' in response.json()

    def test_create_breed_invalid_data(self, auth_client):
        data = {
            'name': '',
            'description': 'Мягкий и пушистый.'
        }

        response = auth_client.post(reverse('breeds-list'), data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'name' in response.json()


@pytest.mark.django_db
class TestCatViews:
    def test_create_cat(self, auth_client):
        breed = BreedFactory()
        data = {
            'name': 'Барсик',
            'age': 4,
            'color': 'Белый',
            'description': 'дружелюбный',
            'breeds': [{'id': breed.id, 'name': breed.name}],
        }
        response = auth_client.post(reverse('cats-list'), data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_cat_missing_name(self, auth_client):
        breed = BreedFactory()
        data = {
            'age': 4,
            'color': 'Белый',
            'description': 'дружелюбный',
            'breeds': [{'id': breed.id, 'name': breed.name}],
        }

        response = auth_client.post(reverse('cats-list'), data=data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'name' in response.json()

    def test_cat_list(self, auth_client):
        CatFactory.create_batch(3)

        response = auth_client.get(reverse('cats-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 3

    def test_retrieve_cat(self, auth_client):
        cat = CatFactory()
        response = auth_client.get(reverse('cats-detail', args=[cat.id]))

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['id'] == cat.id
        assert response.json()['name'] == cat.name

    def test_rate_cat(self, auth_client):
        cat = CatFactory()

        data = {'rate': 5,
                'cat': cat.id}
        response = auth_client.post(reverse('rate'), data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert cat.cat_rates.count() == 1
        assert cat.cat_rates.first().rate == 5

    def test_rate_cat_invalid_rating(self, auth_client):
        cat = CatFactory()

        data = {'rate': 11,
                'cat': cat.id}
        response = auth_client.post(reverse('rate'), data=data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'rate' in response.json()
