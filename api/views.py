from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from rest_framework import viewsets
from requests.api import post
from .models import Log
from .serializers import LogSerializer
import unidecode
import json


base_url = 'http://fernandoabueno.freeddns.org:4567'


def messages(request: HttpRequest):
    if request.method != 'POST':
        return Http404()
    json_parsed = request.body.decode('utf-8')
    delete_logs_if_needed(json_parsed)
    headers = {'Content-Type': 'application/json'}
    unaccented_json_parsed = unidecode.unidecode(json_parsed)
    response = HttpResponse(
        post(f'{base_url}/messages', data=unaccented_json_parsed, headers=headers).content)
    response['Content-Type'] = 'application/json'
    log(request, response)
    return response


def audios(request: HttpRequest):
    if request.method != 'POST':
        return Http404()
    data = {
        'id': request.POST['id']
    }
    files = [
        ('audio', request.FILES['audio'].file)
    ]
    response = HttpResponse(
        post(f'{base_url}/audios', data=data, files=files).content)
    response['Content-Type'] = 'application/json'
    log(request, response)
    return response


def start(request: HttpRequest):
    if request.method != 'POST':
        return Http404()
    json_parsed = request.body.decode('utf-8')
    unaccented_json_parsed = unidecode.unidecode(json_parsed)
    headers = {'Content-Type': 'application/json'}
    response = HttpResponse(
        post(f'{base_url}/start', data=unaccented_json_parsed, headers=headers).content)
    response['Content-Type'] = 'application/json'
    log(request, response)
    return response


def log(request: HttpRequest, response: HttpResponse):
    raw_request_body = request.body.decode('utf-8')
    request_body = json.loads(raw_request_body)

    raw_response_body = response.content.decode('utf-8')

    Log.objects.create(
        telegramId=request_body['id'] if 'id' in request_body else '',
        url=request.build_absolute_uri(),
        request=raw_request_body,
        response=raw_response_body
    )


def delete_logs_if_needed(raw_request_body: str):
    request_body = json.loads(raw_request_body)
    if request_body['message'] == '/reset':
        Log.objects.filter(telegramId=request_body['id']).delete()


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
