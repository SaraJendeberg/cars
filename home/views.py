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
        if (int(received_data["price"])<=0):
            return JsonResponse("Don't enter a negative price or a price of 0. Try again!", safe=False,
                                json_dumps_params={'ensure_ascii': False})
        elif (len(received_data["brand"]) == 0 or len(received_data["model"]) == 0):
            return JsonResponse("Don't enter an empty string. Try again!", safe=False,
                                json_dumps_params={'ensure_ascii': False})
        data = dbfunctions.addNewCarModel(received_data["brand"], received_data["model"], int(received_data["price"]))
        print(data)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii' : False})

