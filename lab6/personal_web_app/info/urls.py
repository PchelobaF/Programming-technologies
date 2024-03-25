from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_index),
    path('info-sort-price', views.info_sort_price_index),
    path('info-sort-name', views.info_sort_name_index),
    path('create', views.create_receipt),
    path('<int:pk>/update', views.InfoUpdateView.as_view(), name='info-update'),
    path('<int:pk>/delete', views.InfoDeleteView.as_view(), name='info-delete'),

]
