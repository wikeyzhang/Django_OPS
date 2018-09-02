# coding: utf-8

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status

from .models import Cabinet, OS, Assets
from .serializers import CabinetSerializers, OSSerializers, ServerListSerializers, ServerDetailSerializers
from .serializers import AssetsSerializers, DevicePortSerializers, ServerAssetsSerializers


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

    def get_queryset(self):
        return Assets.objects.filter(assets_type='server')

 
class ServerCreateViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    服务器创建
    """
    queryset = Assets.objects.all()
    # 重写create 方法
    def create(self, request, *args, **kwargs):
        dict = {}
        data = request.data
        assetsdata = data['assets']
        serverdata = data['server']
        deviceportdata = data['deviceport']
        # 批量创建deviceport
        for i in deviceportdata.keys():
            if deviceportdata[i]:
                serializer = DevicePortSerializers(data=deviceportdata[i])
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                dict[i] = serializer.data
        #创建assets
        serializer = AssetsSerializers(data=assetsdata)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        dict['assets'] = serializer.data
        # 创建server
        for i in dict.keys():
            serverdata[i] = dict[i]['id']
        serializer = ServerAssetsSerializers(data=serverdata)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # 构造返回的数据
        responsedata = serializer.data
        for i in dict.keys():
            responsedata[i] = dict[i]
        headers = self.get_success_headers(responsedata)
        return Response(responsedata, status=status.HTTP_201_CREATED, headers=headers)
