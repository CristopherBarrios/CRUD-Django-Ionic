from django.urls import path
from .views import persona_list, persona_detail, persona_create, persona_update, persona_delete

urlpatterns = [
    path('', persona_list, name='persona_list'),
    path('persona/<int:pk>/', persona_detail, name='persona_detail'),
    path('persona/nueva/', persona_create, name='persona_create'),
    path('persona/<int:pk>/editar/', persona_update, name='persona_update'),
    path('persona/<int:pk>/eliminar/', persona_delete, name='persona_delete'),
]