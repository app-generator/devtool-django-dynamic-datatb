import datetime

from django.db import models
from rest_framework import serializers
import sys
import inspect


class Utils:
    @staticmethod
    def get_class(config, name: str) -> models.Model:
        return Utils.model_name_to_class(config[name])

    @staticmethod
    def get_manager(config, name: str) -> models.Manager:
        return Utils.get_class(config, name).objects

    @staticmethod
    def get_serializer(config, name: str):
        class Serializer(serializers.ModelSerializer):
            class Meta:
                model = Utils.get_class(config, name)
                fields = '__all__'

        return Serializer

    @staticmethod
    def model_name_to_class(name: str):
        all_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        for cls in all_classes:
            if cls[0] == name:
                return cls[1]
        # we are confident that never returns None
        return None


# Create your models here.
class People(models.Model):
    # following two lines is required for all models in this file because models defines outside of app
    # https://docs.djangoproject.com/en/4.0/ref/models/options/#app-label
    class Meta:
        app_label = 'dyn_datatables'

    name = models.CharField(max_length=50)
    age = models.IntegerField()


class Book(models.Model):
    class Meta:
        app_label = 'dyn_datatables'

    title = models.CharField(max_length=100)
    year = models.IntegerField(default=2020)
    is_published = models.BooleanField()


class Sales(models.Model):
    class Meta:
        app_label = 'dyn_datatables'

    product = models.CharField(max_length=100)
    purchase_date = models.DateField(default=datetime.datetime.now())
