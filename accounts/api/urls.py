from django.urls import path
from .views import getRoutes, MyTokenObtainPairView, UserCreateView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', getRoutes, name='routes'),
    path('user/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('user/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', UserCreateView.as_view(), name="signup"),
]
