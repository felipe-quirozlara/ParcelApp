from django.contrib import admin
from django.urls import path, include
import rest_framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parcel.urls', namespace='parcel')),
    path('api/', include('parcel_api.urls', namespace='parcel_api')),
    path('api/user/', include('users.urls', namespace='users')),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
