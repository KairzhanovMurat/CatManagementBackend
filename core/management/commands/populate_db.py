from random import choice

from django.core.management import BaseCommand
from django.db.utils import OperationalError, IntegrityError
from psycopg2 import OperationalError as Psycopg2Error

from main.models import CatRate, Cat, Breed
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('populating database with data...')
        try:
            user1 = User.objects.create_user(email='email@example.com', password='password123', first_name='Админ',
                                             last_name='Админов')
            user2 = User.objects.create_user(email='user2@example.com', password='password123', first_name='Ольга',
                                             last_name='Смирнова')
            user3 = User.objects.create_user(email='user3@example.com', password='password123', first_name='Анна',
                                             last_name='Петрова')

            users = [user1, user2, user3]

            breed1 = Breed.objects.create(name='Сибирская', description='Сильная и пушистая', owner=user1)
            breed2 = Breed.objects.create(name='Персидская', description='Спокойная и красивая', owner=user2)
            breed3 = Breed.objects.create(name='Мейн-кун', description='Большая и дружелюбная', owner=user3)
            breed4 = Breed.objects.create(name='Британская короткошерстная', description='Милая и спокойная',
                                          owner=user1)
            breed5 = Breed.objects.create(name='Бенгальская', description='Энергичная и игривая', owner=user2)

            cats = []
            cat_data = [
                {'name': 'Барсик', 'age': 12, 'color': 'Черный', 'description': 'Любит играть', 'owner': user1,
                 'breed': breed1},
                {'name': 'Мурка', 'age': 24, 'color': 'Белый', 'description': 'Спокойная и милая', 'owner': user2,
                 'breed': breed2},
                {'name': 'Василиса', 'age': 36, 'color': 'Серый', 'description': 'Очень любопытная', 'owner': user3,
                 'breed': breed3},
                {'name': 'Том', 'age': 48, 'color': 'Полосатый', 'description': 'Большой и дружелюбный', 'owner': user1,
                 'breed': breed4},
                {'name': 'Люси', 'age': 18, 'color': 'Рыжий', 'description': 'Игривая и активная', 'owner': user2,
                 'breed': breed5},
                {'name': 'Симба', 'age': 30, 'color': 'Золотой', 'description': 'Король всех котов', 'owner': user3,
                 'breed': breed1},
                {'name': 'Белка', 'age': 20, 'color': 'Белый', 'description': 'Очень игривая', 'owner': user1,
                 'breed': breed2},
                {'name': 'Гарфилд', 'age': 40, 'color': 'Рыжий', 'description': 'Любит поспать', 'owner': user2,
                 'breed': breed3},
                {'name': 'Мышка', 'age': 22, 'color': 'Серебристый', 'description': 'Любит охотиться', 'owner': user3,
                 'breed': breed4},
                {'name': 'Черныш', 'age': 10, 'color': 'Черный', 'description': 'Спокойный и внимательный',
                 'owner': user1, 'breed': breed5},
            ]

            for data in cat_data:
                cat = Cat.objects.create(
                    name=data['name'],
                    age=data['age'],
                    color=data['color'],
                    description=data['description'],
                    owner=data['owner']
                )
                cat.breeds.add(data['breed'])
                cats.append(cat)

            selected_cats = cats[:2]
            for cat in selected_cats:
                cat.breeds.add(breed3)
                for user in users:
                    CatRate.objects.create(rate=choice([3, 4, 5]), user=user, cat=cat)

        except (IntegrityError, OperationalError, Psycopg2Error):
            self.stdout.write(self.style.ERROR('error populating db'))

        self.stdout.write(self.style.SUCCESS('successfully populated db'))
