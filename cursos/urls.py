from django.urls import path
from .views import CursosAPIView,CursoAPIView, AvaliacoesAPIView,AvaliacaoAPIView,CursossAPIView, CursoViewSet, AvaliacaoViewSet
from .views import CursoTitleViewSet
from rest_framework.routers import SimpleRouter
 
router = SimpleRouter()
router.register('cursos',CursoViewSet)
router.register('avaliacoes',AvaliacaoViewSet)
router.register('cursobytitle',CursoTitleViewSet)

urlpatterns = [
    path('cursos/',CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>',CursossAPIView.as_view(),name='curso'),
    path('cursos/<str:titulo>',CursoAPIView.as_view(),name='curso_titulo'),
    path('avaliacoes/<int:pk>',AvaliacaoAPIView.as_view(),name='avaliacao'),
    path('avaliacoes/',AvaliacoesAPIView.as_view(), name='avaliacoes')
]


