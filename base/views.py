from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Movie, Order
from django.views.generic import ListView, DetailView


# Create your views here.

def simpleCheckout(request):
    return render(request, 'base/simple_checkout.html')


def page(request):
    movie = Movie.objects.all()
    context = {'movie': movie}
    return render(request, 'base/MovieApp.html', context)


def checkout(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {'movie': movie}
    return render(request, 'base/checkout.html', context)

def searchbar(request):
    if request.method=='GET':
        search = request.GET.get('search')
        movie = Movie.objects.all().filter(name = search)
    return render(request, 'base/searchbar.html', {'movie': movie})

def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    movie = Movie.objects.get(id=body['movieId'])
    Order.objects.create(
        movie=movie
    )

    return JsonResponse('Payment completed!', safe=False)
