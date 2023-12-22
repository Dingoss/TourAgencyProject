from django.urls import path
from . import views

urlpatterns = [
    path('', views.travellist, name='travellist'),
    path('<int:pk>', views.traveldetail.as_view(), name='traveldetail'),
    path('create_order/', views.create_order, name='create_order')
]
