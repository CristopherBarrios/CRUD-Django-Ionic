from django.urls import path
from .views import PersonaListCreateView, PersonaRetrieveUpdateDestroyView

urlpatterns = [
    path('personas/', PersonaListCreateView.as_view(), name='persona_list_create'),
    path('personas/<int:pk>/', PersonaRetrieveUpdateDestroyView.as_view(), name='persona_retrieve_update_destroy'),
]