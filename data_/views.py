import random # For random generation of an access_code key 
import string # For random generation of an access_code key 
import json # For generating various Python JSON objects 
from os import environ # For adding to mailing list via environment variable CUAPPDEV_INFO_LIST_ID 
from django.shortcuts import render # Classic Django views.py import 
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect # For view responses
from django.template import loader # To load templates 
from django.core.urlresolvers import reverse_lazy, reverse # For generating URLs 
from django.views.generic import View # Standard Generic View 
from django.views.generic.edit import FormView # Generic view used for generating forms
from django.contrib import messages # `flash` messages 
from .models import * # Import all models 
from django.core import serializers # Serializers framework 
from django.core.exceptions import ObjectDoesNotExist # To catch when this happens
from django.contrib import auth  # For logging admin in 
import datetime 
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


@csrf_exempt
def post_data(request): 
    json_data = json.loads(request.body.decode('utf-8'))
    # import ipdb; ipdb.set_trace()
    if json_data.get('data'):
        # try:
        #     target = Data.objects.get(pk=1)
        # except:
        #     print('pk=1 doesnnt exist')
        target = Data()

        target.data_text = json_data.get('data')

        # Populate the object with information 
        target.seconds = json_data.get('seconds')
        target.x_coord = json_data.get('x_coord')
        target.y_coord = json_data.get('y_coord')
        target.z_coord = json_data.get('z_coord')
        target.unknown = json_data.get('unknown')
        target.temp = json_data.get('temp')
        target.eda = json_data.get('eda')
        target.trial = json_data.get('trial')
        target.save() 
        return JsonResponse({ "success": True })
    else: 
        return JsonResponse({ "failure": True })



class Results(View):
    def get(self, request): 
        # Get the data object 
        result = Data.objects.get(pk=1) 
        json_result = { 
                                        "data_text": result.data_text,
                                        "x": result.x_coord,
                                        "y": result.y_coord,
                                        "z": result.z_coord,
                                        "eda": result.eda
                                    }
        return JsonResponse(json_result); 
    





class ResultView(View):


    def get(self, request): 
        template = loader.get_template('results.html')
        context = {}
        return HttpResponse(template.render(context, request))


    def post(self, request): 
        json_data = json.loads(request.body.decode('utf-8'))
        if json_data.get('trial_num'): 
            trial_num = json_data.get('trial_num')
            result = Data.objects.get(pk=1)
            try: 

                trial = Trial.objects.get(pk=trial_num)
                new_data = Data(data_text=result.data_text,
                                                x_coord=result.x_coord,
                                                y_coord=result.y_coord,
                                                z_coord=result.z_coord,
                                                eda=result.eda,
                                                trial=trial_num)

                new_data.save()

            except Exception: 
                trial = Trial(pk=trial_num, name="Trial Number " + str(trial_num), date=datetime.datetime.now())
                trial.save() 

                new_data = Data(data_text=result.data_text,
                                                x_coord=result.x_coord,
                                                y_coord=result.y_coord,
                                                z_coord=result.z_coord,
                                                eda=result.eda,
                                                trial=Trial(name='fixing_bug', date=datetime.now()))

                new_data.save()

            json_result = { 
                                "data_text": result.data_text,
                                "x": result.x_coord,
                                "y": result.y_coord,
                                "z": result.z_coord,
                                "eda": result.eda
                            }

            return JsonResponse(json_result)
        return JsonResponse({ "none": "none" })


@csrf_exempt
def post_graph(request): 
    json_data = json.loads(request.body.decode('utf-8'))
    # if json_data.get('trial_num'): 
    result = Data.objects.all().last() #return last object only

    json_result = { 
                        "data_text": result.data_text,
                        "x": result.x_coord,
                        "y": result.y_coord,
                        "z": result.z_coord,
                        "eda": result.eda
                    }

    return JsonResponse(json_result)
    return JsonResponse({ "none": "none" })










