from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    estimated_time = models.TimeField()
    registered_time = models.TimeField()

    class Meta:
        drf_config = {
            'api': {
                'scaffolding': True
            },
            'serializer': {
                'scaffolding': True
            }
        }
