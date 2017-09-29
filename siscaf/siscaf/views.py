from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View


def index(request):
    return render(request, "home.html")

