from django.urls import path,include
from . import views

urlpatterns = [
    path('add_musician/',views.MusicianCreateView.as_view(), name="add_musician"),
    path('edit_musician/<int:id>/',views.MusicianUpdateView.as_view(), name="edit_musician"),
]
