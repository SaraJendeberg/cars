from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import dbfunctions
import json


# some JSON:
data_dict = [{'name':'John', 'age':30, 'city':'New York'},
             {'name':'Sara', 'age':23, 'city':'Lund'}]


def home(request):
    return JsonResponse("Welcome!", safe=False, json_dumps_params={'ensure_ascii':False}) #safe=False in order to be able to pass non.json object


def employees(request):
    if request.method == "GET":
        data = dbfunctions.getEmployees()
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii':False})


def totalsales(request):
    if request.method == "GET":
        data = dbfunctions.getTotalSales()
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii':False})

@csrf_exempt #bad practice? How could this be solved? discuss?
def carmodels(request):
    if request.method == "GET":
        data = dbfunctions.getCarModels()
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii':False})
    if request.method == "POST":
        received_data = json.loads(request.body) #turn body into dictionary
        data = dbfunctions.addNewCarModel(received_data["brand"], received_data["model"], int(received_data["price"]))
        print(data)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii' : False})

