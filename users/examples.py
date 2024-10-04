from drf_spectacular.utils import OpenApiExample

example_user = OpenApiExample(
    'Пример подробной информации о текущем пользователе',
    value={
        'id': 1,
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'example@email.com'
    },
    response_only=True,
)

example_user_create = OpenApiExample(
    'Пример создания/редактирования информации о текущем пользователе',
    value={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'example@email.com',
        'password': '<PASSWORD>'
    },
    request_only=True,
)
