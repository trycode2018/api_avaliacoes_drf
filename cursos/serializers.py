from rest_framework import serializers
from .models import Curso,Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email':{'write_only':True}
        }
        
        model = Avaliacao
        fields = [
            'id',
            'curso',
            'nome',
            'email',
            'avaliacao',
            'comentario',
            'criacao',
            'ativo'
        ]
        
class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        ]
        
        

