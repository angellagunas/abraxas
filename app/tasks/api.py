# -*- coding: utf-8 -*-
from soft_drf.routing.v1.routers import router

from .viewsets.task import TaskViewSet, TaskSearchViewSet


router.register(
    r"tasks/search",
    TaskSearchViewSet,
    base_name="tasks-search"
)

router.register(
    r"tasks",
    TaskViewSet,
    base_name="tasks"
)
