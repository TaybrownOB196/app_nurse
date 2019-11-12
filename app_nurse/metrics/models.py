from django.db import models
from datetime import datetime

class BaseMetric:
    def __init__(self):
        self.id = None
        self.tags = ''
        self.createDate = None


class AppMetric(BaseMetric):
    def __init__(self):
        super().__init__()
        self.appId = ''
        self.value = ''
        self.dataType = ''

    def to_json(self):
        serfields = ['id', 'appId', 'value', 'dataType', 'tags', 'createDate']
        json = {}
        for field in serfields:
            json[field] =  getattr(self, field)
        return json

    @staticmethod
    def from_dict(dict):
        metric = AppMetric()
        metric.value = dict['value']
        metric.dataType = dict['type']
        metric.tags = dict['tags']
        return metric


class AppDetails:
    def __init__(self):
        self.id = None
        self.appName = ''
        self.description = ''
        self.createDate = None

    def to_json(self):
        serfields = ['id', 'appName', 'description', 'createDate']
        json = {}
        for field in serfields:
            json[field] =  getattr(self, field)
        return json

    @staticmethod
    def from_dict(dict):
        app = AppDetails()
        app.appName = dict['appName']
        app.description = dict['description']
        app.createDate = dict['createDate']
        return app