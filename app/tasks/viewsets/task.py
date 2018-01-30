# -*- coding: utf-8 -*-
from app.tasks.models import Task
from app.tasks.serializers import task as serializers

from rest_framework import status
from rest_framework.response import Response

from soft_drf.api import mixins
from soft_drf.api.viewsets import GenericViewSet


class TaskViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.PartialUpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = serializers.TaskListSerializer
    list_serializer_class = serializers.TaskListSerializer
    retrieve_serializer_class = serializers.TaskListSerializer
    create_serializer_class = serializers.TaskSerializer
    update_serializer_class = serializers.TaskSerializer

    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.all()
        return queryset


class TaskSearchViewSet(GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.TaskListSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        valid_status = ['pendiente', 'completada']
        q = self.request.query_params.get('q', None)
        task_status = self.request.query_params.get('status', None)

        if not q and not task_status:
            return Response(
                'query params is not given',
                status=status.HTTP_400_BAD_REQUEST
            )

        if task_status and task_status.lower() not in valid_status:
            return Response(
                'status is not valid',
                status=status.HTTP_400_BAD_REQUEST
            )

        return super(TaskSearchViewSet, self).list(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.all()
        q = self.request.query_params.get('q', None)
        task_status = self.request.query_params.get('status', None)

        if task_status:
            queryset = queryset.filter(status=task_status.lower())

        if q:
            queryset = queryset.filter(description__icontains=q)

        return queryset
