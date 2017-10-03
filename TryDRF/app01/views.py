# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from app01 import models
# Create your views here.


def publisher_list(request):

    queryset = models.Publisher.objects.all()


    # data = []
    # for i in queryset:
    #     p_tmp = {
    #         "name": i.name,
    #         "address": i.address
    #     }
    #
    #     data.append(p_tmp)


    # data = []
    # from django.forms.models import model_to_dict
    # for i in queryset:
    #     data.append(model_to_dict(i))

    # from django.core import serializers
    #
    # data = serializers.serialize("json", queryset)

    from app01 import serializers

    serializer = serializers.PublisherSerializer(queryset, many=True)

    import json
    return HttpResponse(json.dumps(serializer.data), content_type="application/json")
