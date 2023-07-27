from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action

# ===================== API V1 ===============================
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    
class AvaliacoesAPIView(generics.ListCreateAPIView):
   queryset = Avaliacao.objects.all()
   serializer_class = AvaliacaoSerializer

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    
    
# ===================== API V2 ===============================

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    @action(detail=True,methods=['get'])
    def avaliacoes(self,request,pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(),many=True)
        return Response({'data':serializer.data,'msg':'Avaliacao do curso especificado'})

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    


