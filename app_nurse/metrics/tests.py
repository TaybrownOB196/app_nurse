from django.test import TestCase as djangoTestCase
from unittest import TestCase
from .models import AppDetails, AppMetric
from .services import MetricsService
from app_nurse.lib.crud_helpers import MysqlDbHelper
from datetime import datetime
from json import dumps

class CrudHelperGoodMock(MysqlDbHelper):
    def execute_sproc(self, query):
        return 1, []


class CrudHelperNotFoundMock(MysqlDbHelper):
    def execute_sproc(self, query):
        return 0, []


class ViewsTestCase(TestCase):
    def metrics_invalidVerb_400Response(self):
        pass

    def metrics_invalidPOSTParams_400Response(self):
        pass

    def metrics_invalidPOSTBody_400Response(self):
        pass

    def metrics_invalidGETParams_400Response(self):
        pass

class MetricsServiceTestCase(TestCase):
    def test_service_readById_happypath(self):
        metricsService = MetricsService(CrudHelperGoodMock())
        result = metricsService.read(1)
        self.assertIsNotNone(result)

    def test_service_readById_notfound(self):
        metricsService = MetricsService(CrudHelperNotFoundMock())
        result = metricsService.read(1)
        self.assertIsNone(result)


class ModelsTestCase(TestCase):
    def test_model_hasattr_toJson(self):
        """Assert that the model defines"""
        print('running model_hasattr_toJson')
        self.assertTrue(hasattr(AppMetric(), 'to_json'))
        self.assertTrue(hasattr(AppDetails(), 'to_json'))


    def test_AppMetrictoJson_create_json(self):
        """Tests to ensure json serialization for AppMetric model"""
        print('running AppMetrictoJson_create_json')
        model = AppMetric()
        model.id = 1337
        model.tags = {}
        model.fields = {}
        model.createDate = datetime.now()
        model.appId = 90210
        model.value = 90059
        model.dataType = 'secs'
        json = model.to_json()

        for attr in model.__dict__:
            self.assertEquals(getattr(model, attr), json[attr])

    def test_AppDetailstoJson_create_json(self):
        """Tests to ensure json serialization for AppDetails model"""
        print('running AppDetailstoJson_create_json')
        model = AppDetails()
        model.id = 1337
        model.appName = 'swagger'
        model.description = 'describe the swagger'
        model.createDate = datetime.now()
        json = model.to_json()

        for attr in model.__dict__:
            self.assertEquals(getattr(model, attr), json[attr])

