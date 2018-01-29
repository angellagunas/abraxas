# -*- coding: utf-8 -*-
from app.tasks.models import Task
from app.tasks.serializers import task as serializers

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
    serializer_class = serializers.TaskSerializer
    list_serializer_class = serializers.TaskSerializer
    retrieve_serializer_class = serializers.TaskSerializer
    create_serializer_class = serializers.TaskSerializer
    update_serializer_class = serializers.TaskSerializer

    permission_classes = []  # put your custom permissions here

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.all()
        return queryset
