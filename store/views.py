from django.shortcuts import render
import requests
def store(request):
    return render (request,'store/store.html')
