"""opts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

import xadmin
from assets import views
# from assets.views import CabinetViewSet, OSViewSet, ServerListViewSet, ServerDetailViewSet

# cabinet_list = CabinetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# cabinet_detail = CabinetViewSet.as_view({
#     'get': 'retrieve',
#     'delete': 'destroy'
# })

# os_list = OSViewSet.as_view({
#     'get': 'list'
# })

# server_list = ServerListViewSet.as_view({
#     'get': 'list'
# })

# server_detail = ServerDetailViewSet.as_view({
#     'get': 'retrieve'
# })

router = DefaultRouter()
router.register(r'cabinet', views.CabinetViewSet)
router.register(r'os', views.OSViewSet)
router.register(r'servers', views.ServerListViewSet)
router.register(r'serverdetail', views.ServerDetailViewSet)
router.register(r'servercreate', views.ServerCreateViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),

    url(r'^', include(router.urls))
]

