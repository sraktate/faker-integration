from django.urls import path
from .views import Pagination_show_view, Populate_view

urlpatterns=[
    path('populate/',Populate_view,name='populate'),
    path('pagination/',Pagination_show_view,name='pagination'),
]