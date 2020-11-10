from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from requests.api import post
import json


base_url = 'http://192.168.1.2:4567'


def messages(request: HttpRequest):
    if request.method != 'POST':
        return Http404()
    json_parsed = request.body.decode('utf-8')
    headers = {'Content-Type': 'application/json'}
    response = HttpResponse(
        post(f'{base_url}/messages', data=json_parsed, headers=headers).content)
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
    headers = {'Content-Type': 'application/json'}
    response = HttpResponse(
        post(f'{base_url}/start', data=json_parsed, headers=headers).content)
    response['Content-Type'] = 'application/json'
    return response
