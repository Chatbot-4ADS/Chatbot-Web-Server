from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from requests.api import post
import unidecode
import json


base_url = 'http://fernandoabueno.freeddns.org:4567'


def messages(request: HttpRequest):
    if request.method != 'POST':
        return Http404()
    json_parsed = request.body.decode('utf-8')
    headers = {'Content-Type': 'application/json'}
    unaccented_json_parsed = unidecode.unidecode(json_parsed)
    response = HttpResponse(
        post(f'{base_url}/messages', data=unaccented_json_parsed, headers=headers).content)
    response['Content-Type'] = 'application/json'
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
    return response
