# coding: utf-8

from django.db.models import Count
from rest_framework import serializers

from assets.models import Cabinet, OS, Assets, ServerAssets, DevicePort


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
    server_id = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()
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
        fields = (
        'id', 'server_id', 'sn', 'room', 'cabinet', 'init_u', 'manger', 'mgmt_user', 'mgmt_password', 'mgmt_ip',
        'os', 'model', 'ip', 'device_u', 'up_date')

    def get_server_id(self, obj):
        if obj.assets_ServerAssets.id:
            return obj.assets_ServerAssets.id
        else:
            return ''

    def get_mgmt_user(self, obj):
        if obj.assets_ServerAssets.mgmt_user:
            return obj.assets_ServerAssets.mgmt_user
        else:
            return ''

    def get_room(self, obj):
        choices = {'FG304': '304机房', 'FG308': '308机房', 'BHroom': '506机房', 'HQCroom': '108机房'}
        if obj.cabinet.room:
            return choices[obj.cabinet.room]

    def get_mgmt_password(self, obj):
        if obj.assets_ServerAssets.mgmt_password:
            return obj.assets_ServerAssets.mgmt_password
        else:
            return ''

    def get_mgmt_ip(self, obj):
        if obj.assets_ServerAssets.mgmt_ip:
            return obj.assets_ServerAssets.mgmt_ip
        else:
            return ''

    def get_os(self, obj):
        if obj.assets_ServerAssets.os.name:
            return obj.assets_ServerAssets.os.name
        else:
            return ''

    def get_model(self, obj):
        if obj.assets_ServerAssets.model.name:
            return obj.assets_ServerAssets.model.name
        else:
            return ''

    def get_ip(self, obj):
        if obj.assets_ServerAssets.ip:
            return obj.assets_ServerAssets.ip
        else:
            return ''

    def get_device_u(self, obj):
        if obj.assets_ServerAssets.model.device_u:
            return obj.assets_ServerAssets.model.device_u
        else:
            return ''


class ServerDetailSerializers(serializers.ModelSerializer):
    cabinet = serializers.CharField(source='cabinet.name')
    room = serializers.SerializerMethodField()
    site = serializers.SerializerMethodField()
    manger = serializers.CharField(source='manger.name')
    mgmt_user = serializers.SerializerMethodField()
    mgmt_password = serializers.SerializerMethodField()
    mgmt_ip = serializers.SerializerMethodField()
    os = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    ip = serializers.SerializerMethodField()
    device_u = serializers.SerializerMethodField()
    nic1tosw = serializers.SerializerMethodField()
    nic2tosw = serializers.SerializerMethodField()
    nic3tosw = serializers.SerializerMethodField()
    nic4tosw = serializers.SerializerMethodField()
    nic5tosw = serializers.SerializerMethodField()
    nic6tosw = serializers.SerializerMethodField()
    nic7tosw = serializers.SerializerMethodField()
    nic8tosw = serializers.SerializerMethodField()
    FC01tosw = serializers.SerializerMethodField()
    FC02tosw = serializers.SerializerMethodField()

    class Meta:
        model = Assets
        fields = ('sn', 'cabinet', 'room', 'site', 'init_u', 'manger', 'mgmt_user', 'mgmt_password', 'mgmt_ip', 'os',
                  'model', 'ip', 'device_u', 'nic1tosw', 'nic2tosw', 'nic3tosw', 'nic4tosw', 'nic5tosw', 'nic6tosw',
                  'nic7tosw', 'nic8tosw', 'FC01tosw', 'FC02tosw')

    def get_mgmt_user(self, obj):
        return obj.assets_ServerAssets.mgmt_user

    def get_mgmt_password(self, obj):
        return obj.assets_ServerAssets.mgmt_password

    def get_room(self, obj):
        choices = {'FG304': '304机房', 'FG308': '308机房', 'BHroom': '506机房', 'HQCroom': '108机房'}
        if obj.cabinet.room:
            return choices[obj.cabinet.room]

    def get_site(self, obj):
        choices = {'FG': '东莞', 'BH': '深圳福田', 'HQC': '深圳南山'}
        if obj.cabinet.site:
            return choices[obj.cabinet.site]

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

    def get_nic1tosw(self, obj):
        if obj.assets_ServerAssets.nic1tosw:
            list = [obj.assets_ServerAssets.nic1tosw.net_device.name, obj.assets_ServerAssets.nic1tosw.port_num]
        else:
            list = []
        return list

    def get_nic2tosw(self, obj):
        if obj.assets_ServerAssets.nic2tosw:
            list = [obj.assets_ServerAssets.nic2tosw.net_device.name, obj.assets_ServerAssets.nic2tosw.port_num]
        else:
            list = []
        return list

    def get_nic3tosw(self, obj):
        if obj.assets_ServerAssets.nic3tosw:
            list = [obj.assets_ServerAssets.nic3tosw.net_device.name, obj.assets_ServerAssets.nic3tosw.port_num]
        else:
            list = []
        return list

    def get_nic4tosw(self, obj):
        if obj.assets_ServerAssets.nic4tosw:
            list = [obj.assets_ServerAssets.nic4tosw.net_device.name, obj.assets_ServerAssets.nic4tosw.port_num]
        else:
            list = []
        return list

    def get_nic5tosw(self, obj):
        if obj.assets_ServerAssets.nic5tosw:
            list = [obj.assets_ServerAssets.nic5tosw.net_device.name, obj.assets_ServerAssets.nic5tosw.port_num]
        else:
            list = []
        return list

    def get_nic6tosw(self, obj):
        if obj.assets_ServerAssets.nic6tosw:
            list = [obj.assets_ServerAssets.nic6tosw.net_device.name, obj.assets_ServerAssets.nic6tosw.port_num]
        else:
            list = []
        return list

    def get_nic7tosw(self, obj):
        if obj.assets_ServerAssets.nic7tosw:
            list = [obj.assets_ServerAssets.nic7tosw.net_device.name, obj.assets_ServerAssets.nic7tosw.port_num]
        else:
            list = []
        return list

    def get_nic8tosw(self, obj):
        if obj.assets_ServerAssets.nic8tosw:
            list = [obj.assets_ServerAssets.nic8tosw.net_device.name, obj.assets_ServerAssets.nic8tosw.port_num]
        else:
            list = []
        return list

    def get_FC01tosw(self, obj):
        if obj.assets_ServerAssets.FC01tosw:
            list = [obj.assets_ServerAssets.FC01tosw.net_device.name, obj.assets_ServerAssets.FC01tosw.port_num]
        else:
            list = []
        return list

    def get_FC02tosw(self, obj):
        if obj.assets_ServerAssets.FC02tosw:
            list = [obj.assets_ServerAssets.FC02tosw.net_device.name, obj.assets_ServerAssets.FC02tosw.port_num]
        else:
            list = []
        return list


class ServerAssetsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServerAssets
        fields = ('__all__')


class DevicePortSerializers(serializers.ModelSerializer):
    class Meta:
        model = DevicePort
        fields = ('__all__')


class AssetsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('__all__')
