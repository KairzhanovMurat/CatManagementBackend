import factory
from django.contrib.auth import get_user_model
from main.models import Cat, Breed, CatRate

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')


class BreedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Breed

    name = factory.Sequence(lambda n: f'Breed {n}')
    description = factory.Faker('text', max_nb_chars=100)


class CatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cat

    name = factory.Sequence(lambda n: f'Cat {n}')
    age = factory.Faker('random_int', min=1, max=240)
    color = factory.Faker('color_name')
    description = factory.Faker('text', max_nb_chars=100)
    owner = factory.SubFactory(UserFactory)

    @factory.post_generation
    def breeds(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for breed in extracted:
                self.breeds.add(breed)


class CatRateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CatRate

    rate = factory.Faker('random_int', min=1, max=5)
    user = factory.SubFactory(UserFactory)
    cat = factory.SubFactory(CatFactory)
