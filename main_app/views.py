from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView



class Home(View):

    def get(self, request):
        return HttpResponse("Original G.S Home")
class About(View):

    def get(self, request):
        return HttpResponse("Original G.S About")
