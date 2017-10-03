# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from app01 import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app01 import serializers
# Create your views here.


@api_view(['GET', 'POST'])
def publisher_list(request, format=None):
    """
    列出所有的出版社，或者创建一个新的出版社
    """
    if request.method == "GET":
        queryset = models.Publisher.objects.all()  # 所有的出版社
        s = serializers.PublisherSerializer(queryset, many=True)
        return Response(s.data)

    if request.method == "POST":
        # 创建出版社
        s = serializers.PublisherSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, pk, format=None):
    """
    获取，更新或删除一个出版社实例。
    """
    try:
        publisher = models.Publisher.objects.get(pk=pk)
    except models.Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        s = serializers.PublisherSerializer(publisher)
        return Response(s.data)

    elif request.method == 'PUT':
        s = serializers.PublisherSerializer(publisher, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
