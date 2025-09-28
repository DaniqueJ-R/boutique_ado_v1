from django.urls import path
from . import views, forms

urlpatterns = [
    path('', views.view_bag, name='bag'),
    path('add/<item_id>', forms.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>', forms.adjust_bag, name='adjust_bag'),
    path('delete/<item_id>/', forms.delete_from_bag, name='delete_bag'),
]
