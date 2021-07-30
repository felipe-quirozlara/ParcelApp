from django.urls import path
from .views import EnvioDetail, EnvioList

app_name='parcel_api'

urlpatterns = [
    path('<int:pk>/', EnvioDetail.as_view(), name='EnvioDetail'),
    path('', EnvioList.as_view(), name='EnvioList'),
]
