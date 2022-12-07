from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'cards'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_info, name='view_info'),
    path('add_card/', views.add_card, name='add_card'),
    path('edit_card/<int:id>/', views.edit_card, name='edit_card'),
    path('delete_card/<int:id>/', views.delete_card, name='delete_card'),
    path('search_card/', csrf_exempt(views.search_card), name='search_card'),
]
