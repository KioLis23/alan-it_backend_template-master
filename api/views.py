import csv
from encodings.utf_8 import decode

from django.http import JsonResponse
from rest_framework.utils import json
from rest_framework.views import APIView
import pandas
class GetData(APIView):


    def get(self, request):


        #df = pandas.read_csv('short.csv')
        #data = df.to_json(orient ='values')
        #return JsonResponse(data, safe=False)

        #with open('short.csv', 'rb') as f:
        #    lines = [x.decode().strip() for x in f.readlines()]
        #return JsonResponse(lines, safe=False)

        #with open('./short.csv',encoding='utf-8' ) as f:
        #    for row in csv.reader(f):
        #        encoded = row.encode("UTF-8")
        #        decoded = encoded.decode("UTF-8")
        #return JsonResponse(decoded, safe=False)

        #d = pandas.read_csv('short.csv')
        #df = pandas.DataFrame(d)
        #df = df.to_string()
        #encoded = df.encode("UTF-8")
        #decoded = encoded.decode("UTF-8")
        #return JsonResponse(decoded, safe=False)

        #d = pandas.read_csv('./short.csv')
        #df = pandas.DataFrame(d)
        #da = df.to_string()
        #do = da.encode().decode()
        #return JsonResponse(do, safe=False)

        #with open('short.json', 'r', encoding='utf-8') as f:
        #    data = json.load(f)
        #    return JsonResponse(data, safe=False)



        #with open('short.csv', encoding='utf-8') as f:
        #    d = dict(filter(None, csv.reader(f)))
        #return JsonResponse(d, safe=False)

        flag = True
        response = []
        with open('short.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if flag:
                       names = row
                       flag = False
                       continue
                else:
                       response.append({k: v for k, v in zip(names, row)})
        return JsonResponse(response, safe=False)