from django.urls import path,include
from . import views

urlpatterns = [
    path('add_album/',views.add_album, name="add_album"),
    path('edit_album/<int:id>/',views.edit_album, name="edit_album"),
    path('delete_album/<int:id>/',views.delete_album, name="delete_album"),
]
