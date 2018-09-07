# coding: utf-8

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status

from .models import Cabinet, OS, Assets, DevicePort, ServerAssets
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


class ServerCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
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
        # 创建assets
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


class ServerUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    服务器更新
    """
    queryset = ServerAssets.objects.all()

    # 重写update 方法
    def update(self, request, *args, **kwargs):
        pk = kwargs['pk']
        dict = {}
        data = request.data
        assetsdata = data['assets']
        serverdata = data['server']
        deviceportdata = data['deviceport']
        # 更新deviceport
        server_instance = self.get_object()
        assets_instance = server_instance.assets
        for i in deviceportdata.keys():
            if deviceportdata[i]:
                try:
                    deviceport_id = ServerAssets.objects.values_list(i).get(id=pk)
                    deviceport_instance = DevicePort.objects.get(id=deviceport_id[0])
                    serializer = DevicePortSerializers(deviceport_instance, data=deviceportdata[i])
                except Exception as e:
                    serializer = DevicePortSerializers(data=deviceportdata[i])
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                dict[i] = serializer.data
        # 更新assets
        serializer = AssetsSerializers(assets_instance, data=assetsdata)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        dict['assets'] = serializer.data
        # 创建server
        for i in dict.keys():
            serverdata[i] = dict[i]['id']
        serializer = ServerAssetsSerializers(server_instance, data=serverdata)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # 构造返回的数据
        responsedata = serializer.data
        for i in dict.keys():
            responsedata[i] = dict[i]
        return Response(responsedata, status=status.HTTP_200_OK)


class ServerDeleteViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    删除服务器
    """
    queryset = Assets.objects.all()

    # 重写destroy 方法，按顺序删除 serverassets,assets,deviceport
    def destroy(self, request, *args, **kwargs):
        dict = {}
        # 获取id值
        pk = kwargs['pk']
        instance = ServerAssets.objects.get(id=pk)
        self.perform_destroy(instance)
        assets_instance = Assets.objects.get(id=instance.assets.id)
        self.perform_destroy(assets_instance)
        if instance.nic1tosw:
            dict['nic1tosw_id'] = instance.nic1tosw.id
        if instance.nic2tosw:
            dict['nic2tosw_id'] = instance.nic2tosw.id
        if instance.nic3tosw:
            dict['nic3tosw_id'] = instance.nic3tosw.id
        if instance.nic4tosw:
            dict['nic4tosw_id'] = instance.nic4tosw.id
        if instance.nic5tosw:
            dict['nic5tosw_id'] = instance.nic5tosw.id
        if instance.nic6tosw:
            dict['nic6tosw_id'] = instance.nic6tosw.id
        if instance.nic7tosw:
            dict['nic7tosw_id'] = instance.nic7tosw.id
        if instance.nic8tosw:
            dict['nic8tosw_id'] = instance.nic8tosw.id
        if instance.mgmttosw:
            dict['mgmttosw_id'] = instance.mgmttosw.id
        if instance.FC01tosw:
            dict['FC01tosw_id'] = instance.FC01tosw.id
        if instance.FC02tosw:
            dict['FC02tosw_id'] = instance.FC02tosw.id
        for i in dict.keys():
            instance = DevicePort.objects.get(id=dict[i])
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
