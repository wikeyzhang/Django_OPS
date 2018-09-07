# coding: utf-8
from django.db import models


# Create your models here.


class Cabinet(models.Model):
    """
    机柜
    """
    site_choices = (
        ('FG', u'东莞'),
        ('BH', u'深圳福田'),
        ('HQC', u'深圳南山'),
    )
    room_site_choices = (
        ('FG304', u'304机房'),
        ('FG308', u'308机房'),
        ('BHroom', u'506机房'),
        ('HQCroom', u'108机房'),
    )
    site = models.CharField(choices=site_choices, max_length=100, default='FG308', verbose_name='位置')
    room = models.CharField(choices=room_site_choices, max_length=100, default='FG308', verbose_name='机房')
    name = models.CharField('机柜编号', max_length=16)
    max_u = models.SmallIntegerField('机柜可用U数', blank=True)

    class Meta:
        verbose_name = "机柜"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class OS(models.Model):
    """
    操作系统
    """
    name = models.CharField('操作系统', max_length=16)

    class Meta:
        verbose_name = "操作系统"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ServerModel(models.Model):
    """
    服务器型号
    """
    Server_type_choices = (
        ('hp', u'惠普'),
        ('dell', u'戴尔'),
        ('lenovo', u'联想'),
    )
    server_type = models.CharField(choices=Server_type_choices, max_length=100, default='hp', verbose_name='厂商')
    name = models.CharField('服务器型号', max_length=16)
    device_u = models.SmallIntegerField('设备U数', blank=True)

    class Meta:
        verbose_name = "服务器型号"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DeviceModel(models.Model):
    """
    设备型号
    """
    Device_type_choices = (
        ('cisco', u'思科'),
        ('sangfor', u'深信服'),
        ('H3C', u'华三'),
        ('F5', u'F5公司'),
    )
    device_type = models.CharField(choices=Device_type_choices, max_length=100, default='cisco', verbose_name='厂商')
    name = models.CharField('设备型号', max_length=16)
    device_u = models.SmallIntegerField('设备U数', blank=True)

    class Meta:
        verbose_name = "设备型号"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Manager(models.Model):
    """
     管理员
    """
    name = models.CharField('姓名', max_length=16)

    class Meta:
        verbose_name = "管理员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Assets(models.Model):
    assets_type_choices = (
        ('server', u'服务器'),
        ('switch', u'交换机'),
        ('route', u'路由器'),
        ('firewall', u'防火墙'),
        ('storage', u'存储设备'),
    )
    assets_type = models.CharField(choices=assets_type_choices, max_length=100, default='server', verbose_name='资产类型')
    sn = models.CharField('设备序列号', max_length=100, blank=True, null=True)
    cabinet = models.ForeignKey(Cabinet, related_name='cabinet_Assets', verbose_name='机柜', on_delete=models.SET_NULL,
                                null=True)
    init_u = models.SmallIntegerField('机柜起始U数', blank=True)
    manger = models.ForeignKey(Manager, verbose_name='管理员', on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField('状态', blank=True, null=True)
    up_date = models.DateField('上架时间', blank=True, null=True)

    class Meta:
        verbose_name = "资产信息表"
        verbose_name_plural = verbose_name


class DeviceAssets(models.Model):
    """
    设备表
    """
    assets = models.OneToOneField('Assets', on_delete=models.CASCADE)
    name = models.CharField('设备名称', max_length=32)
    # ip = models.ManyToManyField(IPList)
    ip = models.CharField('IP地址', max_length=32, blank=True, null=True)
    model = models.ForeignKey(DeviceModel, on_delete=models.SET_NULL, verbose_name='设备型号', null=True)

    class Meta:
        verbose_name = "设备信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DevicePort(models.Model):
    """
    设备端口
    """
    port_num = models.CharField('设备端口', max_length=32)
    net_device = models.ForeignKey(DeviceAssets, on_delete=models.CASCADE, verbose_name='网络设备')

    class Meta:
        verbose_name = "设备端口"
        verbose_name_plural = verbose_name


class ServerAssets(models.Model):
    """
    服务器
    """
    assets = models.OneToOneField('Assets', related_name='assets_ServerAssets', on_delete=models.CASCADE)
    # ip = models.ManyToManyField(IPList)
    ip = models.CharField('业务IP地址', max_length=32, blank=True, null=True)
    nic1tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter01',
                                    on_delete=models.SET_NULL, verbose_name='网口1对应设备端口')
    nic2tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter02',
                                    on_delete=models.SET_NULL, verbose_name='网口2对应设备端口')
    nic3tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter03',
                                    on_delete=models.SET_NULL, verbose_name='网口3对应设备端口')
    nic4tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter04',
                                    on_delete=models.SET_NULL, verbose_name='网口4对应设备端口')
    nic5tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter05',
                                    on_delete=models.SET_NULL, verbose_name='网口5对应设备端口')
    nic6tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter06',
                                    on_delete=models.SET_NULL, verbose_name='网口6对应设备端口')
    nic7tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter07',
                                    on_delete=models.SET_NULL, verbose_name='网口7对应设备端口')
    nic8tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter08',
                                    on_delete=models.SET_NULL, verbose_name='网口8对应设备端口')
    mgmttosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter09',
                                    on_delete=models.SET_NULL, verbose_name='管理网口对应设备端口')
    FC01tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter10',
                                    on_delete=models.SET_NULL, verbose_name='FC01网口对应设备端口')
    FC02tosw = models.OneToOneField(DevicePort, blank=True, null=True, related_name='ohter11',
                                    on_delete=models.SET_NULL, verbose_name='FC02网口对应设备端口')
    # mgmt_ip = models.ForeignKey(IPList, blank=True, null=True, related_name='ohter12', on_delete=models.SET_NULL,
    #                             verbose_name='管理IP地址')
    mgmt_ip = models.CharField('管理IP地址', max_length=32, blank=True, null=True)
    mgmt_user = models.CharField('管理用户', max_length=16, blank=True, null=True)
    mgmt_password = models.CharField('管理密码', max_length=16, blank=True, null=True)
    model = models.ForeignKey(ServerModel, on_delete=models.SET_NULL, null=True, verbose_name='服务器型号')
    os = models.ForeignKey(OS, related_name='os_ServerAssets', verbose_name='操作系统', on_delete=models.SET_NULL,
                           null=True)

    class Meta:
        verbose_name = "服务器信息"
        verbose_name_plural = verbose_name
