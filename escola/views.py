from django.shortcuts import render
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, \
    MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunoMatriculadoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os aluno'''
    queryset = Aluno.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculaViewSet(viewsets.ModelViewSet):
    '''Listando todas as matriculas'''
    queryset = Matricula.objects.all()
    
    serializer_class = MatriculaSerializer
    http_method_names = ['GET', 'PUT', 'POST', 'DELETE']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    '''Listando as matriculas de uma aluno especifico'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasAlunoSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    '''Listando todos os alunos matriculados em um curso especifico'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaAlunoMatriculadoSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

