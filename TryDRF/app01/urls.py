#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/4

from django.conf.urls import url, include
from app01 import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url('^schema/$', schema_view),
    url(r'docs/', include_docs_urls(title="图书管理系统")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
