from drf_spectacular.utils import OpenApiExample

example_cat_list = [
    OpenApiExample(
        'Пример списка кошек',
        value=[
            {
                'id': 1,
                'name': 'Барсик',
                'age': 24,
                'color': 'Серый',
                'owner': 'John Doe',
                'breeds': ['шотландец', 'британец'],
                'average_rating': 4.5
            },
            {
                'id': 2,
                'name': 'Мурзик',
                'age': 12,
                'color': 'Черный',
                'owner': 'Foo Bar',
                'breeds': ['уличный'],
                'average_rating': 0
            }
        ],
        response_only=True,
    ),
]

example_cat_detail = OpenApiExample(
    'Пример подробной информации о кошке',
    value={
        'id': 1,
        'name': 'Барсик',
        'age': 24,
        'color': 'Серый',
        'owner': 'John Doe',
        'breeds': ['шотландец', 'британец'],
        'average_rating': 4.5,
        'description': 'умный и ласковый кот'
    },
    response_only=True,
)

example_cat_create = OpenApiExample(
    'Пример создания/редактирования информации о кошке',
    value={
        'name': 'Барсик',
        'age': 24,
        'color': 'Серый',
        'breeds': [{'name': 'британец'}],
        'description': 'умный и ласковый кот'
    },
    request_only=True,
)

example_breed_list = [
    OpenApiExample(
        'Пример списка пород',
        value=[
            {
                'id': 1,
                'name': 'шотландец',
                'owner': 'John Doe',

            },
            {
                'id': 2,
                'name': 'мейнкун',
                'owner': 'Foo Bar',
            }
        ],
        response_only=True,
    ),
]

example_breed_detail = OpenApiExample(
    'Пример подробной информации о породе',
    value={
        'id': 1,
        'name': 'шотландец',
        'owner': 'John Doe',
        'description': 'спокойные, не любят ласку '

    },
    response_only=True,
)

example_breed_create = OpenApiExample(
    'Пример создания/редактирования информации о породе',
    value={
        'name': 'шотландец',
        'description': 'спокойные, не любят ласку '
    },
    request_only=True,
)

example_cat_rate = OpenApiExample(
    'Пример создания оценки кошки',
    value={
        'rate': 5,
        'cat': 1
    },
    request_only=True,
)
