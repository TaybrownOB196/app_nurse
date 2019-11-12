from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View

from app_nurse.lib.crud_helpers import MysqlDbHelper
from app_nurse.lib.json_helpers import CustomEncoder
from app_nurse.metrics.services import MetricsService, AppService

from app_nurse.metrics.models import AppMetric, AppDetails

import json


metrics_srvc = MetricsService(MysqlDbHelper())
app_srvc = AppService(MysqlDbHelper())


class DefaultView(View):
    def get(self, request):
        results = app_srvc.read()
        return render(request, 'default.html', {"applications": results})    


class MetricView(View):
    def post(self, request: HttpRequest):
        appId = request.GET.get('appId', None)
        if appId is None and not request.body:
            return HttpResponse(content=b'bad request', status=400)
            
        body = request.body.decode('utf-8')
        json_body = json.loads(body)
        if json_body is not None:
            metric = AppMetric.from_dict(json_body)

            new_metric = metrics_srvc.save(appId, metric)
            if new_metric is not None:
                #return HttpResponse(content=json.dumps(metric, cls=CustomEncoder), status=201)
                return HttpResponse(content=json.dumps(new_metric, cls=CustomEncoder), status=201)
            else:
                return HttpResponse(status=500)

        return HttpResponse(content=b'bad request', status=400)
        

    def get(self, request: HttpRequest):
        results = None
        appId = request.GET.get('appId', None)
        metricId = request.GET.get('metricId', None)
        if appId is None:
            return HttpResponse(content=b'bad request', status=400)

        if metricId is None:
            results = metrics_srvc.read(appId)
        else:
            results = metrics_srvc.readLatest(appId, metricId)

        if results is None:
            return HttpResponse(content=b'no content', status=204)
        else:
            return HttpResponse(content=json.dumps(results, cls=CustomEncoder), status=200)


class ApplicationView(View):
    def post(self, request: HttpRequest):
        body = request.body.decode('utf-8')
        json_body = json.loads(body)
        if json_body is None:
            return HttpResponse(content=b'bad request', status=400)

        else:
            app = AppDetails()
            app.appName = json_body['applicationName']
            app.description = json_body['applicationDescription']
            new_app = app_srvc.save(app)
            return HttpResponse(content=json.dumps(new_app, cls=CustomEncoder), status=201)


    def get(self, request: HttpRequest):
        results = None
        appId = request.GET.get('appId', None)

        if appId is None:
            results = app_srvc.read()

        else:
            app = app_srvc.readById(appId)
            metrics = metrics_srvc.read(appId)
            return render(request, 'application.html', {"app": app, "metrics": metrics, "metricsStr": json.dumps(metrics, cls=CustomEncoder)})
        
        if results is None:
            return HttpResponse(content=b'no content', status=204)
        else:
            return HttpResponse(content=json.dumps(results, cls=CustomEncoder), status=200)