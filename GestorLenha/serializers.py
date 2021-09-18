from django.contrib.auth.models import User, Group
from rest_framework import serializers
from GestorLenha.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
               class Meta:
                              model = User
                              fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
               class Meta:
                              model = Group
                              fields = ['url', 'name']

class EncomendaSerializer(serializers.HyperlinkedModelSerializer):
               class Meta:
                              model = Encomenda
                              fields = [
                                             'data_entrega', 
                                             'quantidade',
                                             'cliente',
                                             'preco', 
                                             'morada_entrega', 
                                             'estado'
                                             ]
