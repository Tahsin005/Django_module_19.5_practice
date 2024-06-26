from django.urls import path 
from . import views
urlpatterns = [
    path('create_album/', views.create_album, name="create_album"),
    path('edit_album/<int:id>', views.edit_album, name='edit_album'),
    path('delete_album/<int:id>', views.delete_album, name='delete_album'),
]
