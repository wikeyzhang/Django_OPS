# coding: utf-8

from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .models import Cabinet, OS, Assets
from .serializers import CabinetSerializers, OSSerializers, ServerListSerializers, ServerDetailSerializers


class CabinetViewSet(viewsets.ModelViewSet):
    """
    机房位置
    """
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializers


class OSViewSet(viewsets.ModelViewSet):
    """
    OS系统
    """
    queryset = OS.objects.all()
    serializer_class = OSSerializers


class ServerListViewSet(viewsets.ModelViewSet):
    """
    服务器列表
    """
    queryset = Assets.objects.all()
    serializer_class = ServerListSerializers

    def get_queryset(self):
        return Assets.objects.filter(assets_type='server')


class ServerDetailViewSet(viewsets.ModelViewSet):
    """
    服务器详情
    """
    queryset = Assets.objects.all()
    serializer_class = ServerDetailSerializers