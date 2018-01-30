# -*- coding: utf-8 -*-
from app.tasks.models import Task

from rest_framework import serializers

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

    def validate(self, data):
        request = self.context.get('request')

        if request.method == 'PATCH':
            task_status = data.get('status', None)

            if task_status and self.instance.status == 'completada':
                raise serializers.ValidationError(
                    "The given task can't be updated"
                )

        return data
