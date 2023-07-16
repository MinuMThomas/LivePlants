from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/<int:item_id>', views.reviews, name='reviews'),
    path('reviews/add_review/<int:item_id>', 
         views.add_review, name='add_review'),
]
