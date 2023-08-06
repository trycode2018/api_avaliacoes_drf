from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

 
# ===================== API V1 ===============================
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
            
        #return super().get_object()
class CursossAPIView(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'titulo'
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveAPIView):
    lookup_field = 'titulo'
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    def get_object(self):
        if self.kwargs.get('titulo'):
            return self.queryset.filter(titulo=self.kwargs.get('titulo')).first()
        return self.queryset.all()
    
class AvaliacoesAPIView(generics.ListCreateAPIView):
   queryset = Avaliacao.objects.all()
   serializer_class = AvaliacaoSerializer
   
   #def get_queryset(self):
   #    if self.kwargs.get('titulo'):
   #        return self.queryset.filter(nome=self.kwargs.get(lookup_field))
   #    return self.queryset.all()

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
class CursoTitleViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    lookup_field = 'titulo'
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    def get_object(self):
        if self.kwargs.get('titulo'):
            return self.queryset.filter(titulo=self.kwargs.get('titulo')).first()
        return self.queryset.all()

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    
    
    


