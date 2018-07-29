from django.db import models

# Create your models here.
class Cabinet(models.Model):
    """
    机柜
    """
    name = models.CharField('编号', max_length=16)
    def __str__(self):
        return self.name

class Brand(models.Model):
    """
    厂商
    """
    name = models.CharField('厂商 ', max_length=16)
    def __str__(self):
        return self.name
class OS(models.Model):
    """
    操作系统
    """
    name = models.CharField('操作系统', max_length=16)
    def __str__(self):
        return self.name

class init_u_num(models.Model):
    """
    机柜起始U数
    """
    u_num = models.CharField('机柜起始U数',max_length=16)
    def __str__(self):
        return self.u_num

class device_u_num(models.Model):
    """
    设备U数
    """
    u_num = models.CharField('设备U数',max_length=16)
    def __str__(self):
        return self.u_num

class Model(models.Model):
    """
    服务器、设备型号
    """
    name = models.CharField('服务器型号', max_length=16)
    def __str__(self):
        return self.name
class IP_list(models.Model):
     """
      IP地址
     """  
    IPaddress= models.CharField('IP地址', max_length=32)
    def __str__(self):
        return self.IPaddress

class Type(models.Model):
    """
    设备类型
    """
    name = models.CharField('设备类型', max_length=16)
    def __str__(self):
        return self.name

class Device(models.Model):
    """
    设备表
    """
    name = models.CharField('设备名称', max_length=32)
    #cabinet = models.ForeignKey(Cabinet, verbose_name='机柜')
    #serial_num = models.CharField('序列号', max_length=16)
    ip = models.ManyToManyField(IP_list)
    #brand = models.ForeignKey(Brand, verbose_name='厂商')
    #init_u = models.ForeignKey(init_u_num, verbose_name='机柜起始U数')
    #device_u = models.ForeignKey(device_u_num, verbose_name='设备U数')
    model = models.ForeignKey(Model, verbose_name='设备型号')
    net_type = models.ForeignKey(Type, verbose_name='设备类型')
    def __str__(self):
        return self.name

class Device_port(models.Model):
    """
    设备端口
    """
    port_num = models.CharField('设备端口', max_length=32)
    net_device=models.ForeignKey(Device , on_delete=models.CASCADE,verbose_name='网络设备')



class Servers(models.Model):
    """
    服务器
    """
    #name = models.CharField('序列号', max_length=16)
    #ip = models.ForeignKey(IP_list,blank=True,null=True,related_name='ohter03')
    ip = models.ManyToManyField(IP_list)
    nic1tosw = models.OneToOneField(Device_port,null=True,related_name='ohter01',on_delete=models.SET_NULL,verbose_name='网口1对应设备端口')
    nic2tosw = models.OneToOneField(Device_port,null=True,related_name='ohter02',on_delete=models.SET_NULL,verbose_name='网口2对应设备端口')
    nic3tosw = models.OneToOneField(Device_port,null=True,related_name='ohter03',on_delete=models.SET_NULL,verbose_name='网口3对应设备端口')
    nic4tosw = models.OneToOneField(Device_port,null=True,related_name='ohter04',on_delete=models.SET_NULL,verbose_name='网口4对应设备端口')
    nic5tosw = models.OneToOneField(Device_port,null=True,related_name='ohter05',on_delete=models.SET_NULL,verbose_name='网口5对应设备端口')
    nic6tosw = models.OneToOneField(Device_port,null=True,related_name='ohter06',on_delete=models.SET_NULL,verbose_name='网口6对应设备端口')
    nic7tosw = models.OneToOneField(Device_port,null=True,related_name='ohter07',on_delete=models.SET_NULL,verbose_name='网口7对应设备端口')
    nic8tosw = models.OneToOneField(Device_port,null=True,related_name='ohter08',on_delete=models.SET_NULL,verbose_name='网口8对应设备端口')
    mgmttosw = models.OneToOneField(Device_port,null=True,related_name='ohter09',on_delete=models.SET_NULL,verbose_name='管理网口对应设备端口')
    FC01tosw = models.OneToOneField(Device_port,null=True,related_name='ohter10',on_delete=models.SET_NULL,verbose_name='FC01网口对应设备端口')
    FC02tosw = models.OneToOneField(Device_port,null=True,related_name='ohter11',on_delete=models.SET_NULL,verbose_name='FC02网口对应设备端口')
    mgmt_ip = models.ForeignKey(IP_list ,null=True,related_name='ohter12',on_delete=models.SET_NULL,verbose_name='管理IP地址')
    mgmt_user = models.CharField('管理用户', max_length=16)
    mgmt_password = models.CharField('管理密码', max_length=16)
   # brand = models.ForeignKey(Brand, verbose_name='厂商')
   # cabinet = models.ForeignKey(Cabinet, verbose_name='机柜')
    #init_u = models.ForeignKey(init_u_num, verbose_name='机柜起始U数')
    #device_u = models.ForeignKey(device_u_num, verbose_name='设备U数')
    model = models.ForeignKey(Model, verbose_name='服务器型号')
    os = models.ForeignKey(OS, verbose_name='操作系统')

class Assets(models.Model):
    assets_type_choices = (
                          ('server',u'服务器'),
                          ('switch',u'交换机'),
                          ('route',u'路由器'),
                          ('firewall',u'防火墙'),
                          ('storage',u'存储设备'),
                          )
    assets_type = models.CharField(choices=assets_type_choices,max_length=100,default='server',verbose_name='资产类型')
    name = models.CharField(max_length=100,verbose_name='资产编号',unique=True)
    sn =  models.CharField(max_length=100,verbose_name='设备序列号',blank=True,null=True)
    brand = models.ForeignKey(Brand, verbose_name='厂商')
    cabinet = models.ForeignKey(Cabinet, verbose_name='机柜')
    init_u = models.ForeignKey(init_u_num, verbose_name='机柜起始U数')
    device_u = models.ForeignKey(device_u_num, verbose_name='设备U数')
#    def __str__(self):
#        return self.name