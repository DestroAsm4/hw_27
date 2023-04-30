import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import csv

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import ADS, Categories

@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):

    def get(self, request):

        categories = Categories.objects.all()

        response = []
        for category in categories:
            response.append({
                'id': category.id,
                'name': category.name,
            })
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):

        category_data = json.loads(request.body)
        category = Categories()
        category.name = category_data['name']
        category.save()
        return JsonResponse({
            'id': category.id,
            'name': category.name,
        }, safe=False, status=200)

class CategoryDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):

        category = self.get_object()

        response = {
                'id': category.id,
                'name': category.name,
            }

        return JsonResponse(response, safe=False, status=200)

@method_decorator(csrf_exempt, name="dispatch")
class ADSView(View):
    def get(self, request):
        ads = ADS.objects.all()
        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
            })
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        ads_data = json.loads(request.body)
        ads = ADS()
        ads.name = ads_data['name']
        ads.author = ads_data['author']
        ads.price = int(ads_data['price'])
        ads.description = ads_data['description']
        ads.address = ads_data['address']
        ads.is_published = bool(ads_data['is_published'])
        ads.save()
        return JsonResponse({
                'id': ads.id,
                'name': ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
            }, safe=False, status=200)

class ADSDetailView(DetailView):
    model = ADS

    def get(self, request, *args, **kwargs):

        ads = self.get_object()

        response = {
                'id': ads.id,
                'name': ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
            }

        return JsonResponse(response, safe=False, status=200)

@csrf_exempt
def csv_to_django_db(request):

    with open('categories.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        for row in rows:
            categories = Categories()
            categories.name = row['name']
            categories.save()

    with open('ads.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        for row in rows:
            ads = ADS()
            ads.name = row['name']
            ads.author = row['author']
            ads.price = int(row['price'])
            ads.description = row['description']
            ads.address = row['address']
            ads.is_published = bool(row['is_published'])
            ads.save()

    return JsonResponse({'status': "ok"}, status=200)




def hello(request):

    return JsonResponse({'status': "ok"}, status=200)
# Create your views here.
