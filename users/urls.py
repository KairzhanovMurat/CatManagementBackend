from django.urls import path


from . import views

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('me/', views.ManageCurrentUserView.as_view(), name='me'),
    path('token/', views.TokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.RefreshView.as_view(), name='token_refresh'),
]
