from django.urls import path
from . import views

urlpatterns = [
   path('', views.item_form, name="item_insert"),
   path('<int:id>/', views.item_form, name="item_update"),
   path('delete/<int:id>/', views.item_delete, name="item_delete"),
   path('list/', views.item_list, name="item_list"),

   # path('item', views.item_list),
   # path('item/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
   # path('create', views.ItemCreate.as_view(), name='item_create'),
   # path('update/<int:pk>', views.ItemUpdate.as_view(), name='item_update'),
   # path('delete/<int:pk>', views.ItemDelete.as_view(), name='item_delete'),
   
]
