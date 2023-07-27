from django.urls import path
from .views import CursosAPIView,CursoAPIView, AvaliacoesAPIView,AvaliacaoAPIView, CursoViewSet, AvaliacaoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos',CursoViewSet)
router.register('avaliacoes',AvaliacaoViewSet)

urlpatterns = [
    path('cursos/',CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>',CursoAPIView.as_view(),name='curso'),
    path('avaliacoes/<int:pk>',AvaliacaoAPIView.as_view(),name='avaliacao'),
    path('avaliacoes/',AvaliacoesAPIView.as_view(), name='avaliacoes')
]
