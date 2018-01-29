# -*- coding: utf-8 -*-
from app.tasks.models import Task

from soft_drf.api.serializers import ModelSerializer


class TaskListSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'id',
            'description',
            'status',
            'estimated_time',
            'registered_time',
        )


class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'description',
            'status',
            'estimated_time',
            'registered_time',
        )
