from django.http import HttpResponse
from django.shortcuts import render

def new_profile(request):
    context = {"fields": ["username","pin","email","website","address","alias"]}
    return HttpResponse(render(request, 'profiles/new.html', context))