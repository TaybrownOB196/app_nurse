from .models import AppMetric, AppDetails
from app_nurse.lib.crud_helpers import MysqlDbHelper
import json

class AppService:
    def __init__(self, crud_helper):
        self.crud_helper = crud_helper

    def read(self):
        query_str = 'call temp.getAppServices();'
        count, data = self.crud_helper.execute_sproc(query_str)
        print(count)
        if count > 0:
            print(data)
            return data
        
        return None

    def readById(self, appId):
        query_str = 'call temp.getAppServicesById(%s);' % (appId)
        count, data = self.crud_helper.execute_sproc(query_str)
        print(count)
        if count > 0:
            print(data)
            return data

        return None

    def readByName(self, applicationName):
        query_str = 'call temp.getAppServicesByName(\'%s\');' % (applicationName)
        count, data = self.crud_helper.execute_sproc(query_str)
        print(count)
        if count > 0:
            print(data)
            return data

        return None

    def save(self, obj):
        query_str = 'call temp.saveAppService(\'%s\', \'%s\');' % (obj.appName, obj.description)
        count, data = self.crud_helper.execute_sproc(query_str)
        if count == 1:
            obj.id = data[0]['id']
            return obj
        
        return None


class MetricsService:
    def __init__(self, crud_helper):
        self.crud_helper = crud_helper

    def read(self, appId):
        query_str = 'call temp.getMetricsByAppId(%s);' % (appId)
        count, data = self.crud_helper.execute_sproc(query_str)
        if count > 0:
            print(data)
            return data

        return None

    def readLatest(self, appId, metricId):
        query_str = 'call temp.getMetricsByAppIdPastMetricId(%s, %s);' % (appId, metricId)
        count, data = self.crud_helper.execute_sproc(query_str)
        if count > 0:
            return data

        return None

    def save(self, appId, metric):
        query_str = 'call temp.saveMetric(%s, \'%s\', \'%s\', \'%s\');' % (appId, metric.value, metric.dataType, metric.tags)
        count, data = self.crud_helper.execute_sproc(query_str)
        if count == 1:
            metric.id = data[0]['id']
            return metric

        return None