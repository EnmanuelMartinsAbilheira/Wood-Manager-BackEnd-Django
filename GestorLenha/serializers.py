from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from GestorLenha.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'pk']


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EncomendaSerializer(serializers.HyperlinkedModelSerializer):
    username = ReadOnlyField(source="cliente.username")
    class Meta:
        model = Encomenda
        fields = [
            'data_entrega',
            'quantidade',
            #'cliente',
            'username',
            'preco',
            'morada_entrega',
            'estado',
            'pk',
            'is_deleted'
        ]

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(EncomendaSerializer, self).__init__(*args, **kwargs)


class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = [
            'preco_tonelada'
        ]