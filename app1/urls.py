from django.urls import path
from .views import add_person, table

urlpatterns = [
    path('', add_person, name='add_person'),
    # path('success/', success, name='success'),
    path('table/', table, name='table'),
]