# coding: utf-8

import xadmin

from .models import DeviceAssets, ServerAssets, Assets, Cabinet, OS, ServerModel
from .models import DeviceModel, Manager, DevicePort


class DeviceAssetsAdmin(object):
    list_display = ['assets', 'ip', 'name', 'model']
    search_fields = ['ip', 'name', 'model']
    list_filter = ['ip', 'name', 'model']


class ServerAssetsAdmin(object):
    list_display = ['assets', 'ip', 'nic1tosw', 'nic2tosw', 'nic3tosw', 'nic4tosw', 'nic5tosw', 'nic6tosw', 'nic7tosw',
                    'nic8tosw', 'mgmttosw', 'FC01tosw', 'FC02tosw', 'mgmt_ip', 'mgmt_user', 'mgmt_password', 'model',
                    'os']
    search_fields = ['ip', 'mgmt_ip']
    list_filter = ['ip', 'mgmt_ip']


class AssetsAdmin(object):
    list_display = ['assets_type', 'name', 'sn', 'cabinet', 'init_u', 'manger', 'status', 'up_date']
    search_fields = ['assets_type', 'name', 'sn', 'cabinet', 'manger', 'status']
    list_filter = ['assets_type', 'name', 'sn', 'cabinet', 'manger', 'status']


class OSAdmin(object):
    list_display = ['name']


class ManagerAdmin(object):
    list_display = ['name']


class IPListAdmin(object):
    list_display = ['IP_address']


class DevicePortAdmin(object):
    list_display = ['port_num', 'net_device']
    search_fields = ['net_device']
    list_filter = ['net_device']


class ServerModelAdmin(object):
    list_display = ['server_type', 'device_u', 'name']
    search_fields = ['server_type', 'device_u', 'name']
    list_filter = ['server_type', 'device_u']


class DeviceModelAdmin(object):
    list_display = ['device_type', 'device_u', 'name']
    search_fields = ['device_type', 'device_u', 'name']
    list_filter = ['device_type', 'device_u']


class CabinetAdmin(object):
    list_display = ['site', 'room', 'name']
    search_fields = ['site', 'room', 'name']
    list_filter = ['site', 'room']


xadmin.site.register(DeviceAssets, DeviceAssetsAdmin)
xadmin.site.register(ServerAssets, ServerAssetsAdmin)
xadmin.site.register(Assets, AssetsAdmin)
xadmin.site.register(Cabinet, CabinetAdmin)
xadmin.site.register(OS, OSAdmin)
xadmin.site.register(ServerModel, ServerModelAdmin)
xadmin.site.register(Manager, ManagerAdmin)
xadmin.site.register(DevicePort, DevicePortAdmin)
xadmin.site.register(DeviceModel, DeviceModelAdmin)
