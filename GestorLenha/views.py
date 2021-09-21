from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets,permissions
from GestorLenha.models import *
from GestorLenha.serializers import *

def HttpResponse_json(data):
               try:
                              data = serializers.serialize('json', data)
               except:
                              pass
               return HttpResponse(data, content_type='application/json')




class UserViewSet(viewsets.ModelViewSet):
               """
               API endpoint that allows users to be viewed or edited.
               """
               queryset = User.objects.all().order_by('-date_joined')
               serializer_class = UserSerializer
               permissizon_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
               """
               API endpoint that allows groups to be viewed or edited.
               """
               queryset = Group.objects.all()
               serializer_class = GroupSerializer
               permission_classes = [permissions.IsAuthenticated]

class encomendas_view(viewsets.ModelViewSet):
               queryset = Encomenda.objects.all()
               serializer_class = EncomendaSerializer
               permission_classes = [permissions.IsAuthenticated]
