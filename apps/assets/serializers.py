# coding: utf-8

from django.db.models import Count
from rest_framework import serializers

from assets.models import Cabinet, OS, Assets, ServerAssets


class CabinetSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cabinet
        fields = ('id', 'name', 'room', 'site', 'max_u')


class OSSerializers(serializers.ModelSerializer):
    os_server_count = serializers.SerializerMethodField()

    class Meta:
        model = OS
        fields = ('id', 'name', 'os_server_count')

    def get_os_server_count(self, obj):
        counts = obj.os_ServerAssets.values_list('os').annotate(Count('id'))
        if counts:
            os_server_count = counts[0][1]
        else:
            os_server_count = 0
        return os_server_count


class ServerListSerializers(serializers.ModelSerializer):
    cabinet = serializers.CharField(source='cabinet.name')
    manger = serializers.CharField(source='manger.name')
    mgmt_user = serializers.SerializerMethodField()
    mgmt_password = serializers.SerializerMethodField()
    mgmt_ip = serializers.SerializerMethodField()
    os = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    ip = serializers.SerializerMethodField()
    device_u = serializers.SerializerMethodField()

    class Meta:
        model = Assets
        fields = ('sn', 'cabinet', 'init_u', 'manger', 'mgmt_user', 'mgmt_password', 'mgmt_ip',
                  'os', 'model', 'ip', 'device_u', 'up_date')

    def get_mgmt_user(self, obj):
        return obj.assets_ServerAssets.mgmt_user

    def get_mgmt_password(self, obj):
        return obj.assets_ServerAssets.mgmt_password

    def get_mgmt_ip(self, obj):
        return obj.assets_ServerAssets.mgmt_ip

    def get_os(self, obj):
        return obj.assets_ServerAssets.os.name

    def get_model(self, obj):
        return obj.assets_ServerAssets.model.name

    def get_ip(self, obj):
        return obj.assets_ServerAssets.ip

    def get_device_u(self, obj):
        return obj.assets_ServerAssets.model.device_u


class ServerDetailSerializers(serializers.ModelSerializer):
    cabinet = serializers.CharField(source='cabinet.name')
    manger = serializers.CharField(source='manger.name')
    mgmt_user = serializers.SerializerMethodField()
    mgmt_password = serializers.SerializerMethodField()
    mgmt_ip = serializers.SerializerMethodField()
    os = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    ip = serializers.SerializerMethodField()

    class Meta:
        model = Assets
        fields = ('sn','cabinet', 'init_u', 'manger', 'mgmt_user', 'mgmt_password', 'mgmt_ip','os',
                  'model', 'ip', 'nic1tosw', 'nic2tosw', 'nic3tosw', 'nic4tosw', 'nic5tosw', 'nic6tosw',
                  'nic7tosw', 'nic8tosw', 'FC01tosw', 'FC02tosw')

    def get_mgmt_user(self, obj):
        return obj.assets_ServerAssets.mgmt_user

    def get_mgmt_password(self, obj):
        return obj.assets_ServerAssets.mgmt_password

    def get_mgmt_ip(self, obj):
        return obj.assets_ServerAssets.mgmt_ip

    def get_os(self, obj):
        return obj.assets_ServerAssets.os.name

    def get_model(self, obj):
        return obj.assets_ServerAssets.model.name

    def get_ip(self, obj):
        return obj.assets_ServerAssets.ip
