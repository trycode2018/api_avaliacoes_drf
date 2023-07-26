from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.validators import UnicodeUsernameValidator

class CursoAPIView(APIView):
    
    def validate_password(self,value):
        if len(value)<10:
            raise ValidationError('A senha deve ter no minimo 8 caracteres')
    
    
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self,request):
       
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'msg':'Curso criado com sucesso','data':serializer.data},
                        status=status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):
    
    def get(self,request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'msg':'Avaliacao criada com sucesso','data':serializer.data},
                        status=status.HTTP_201_CREATED)
    
