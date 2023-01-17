from django.shortcuts import render
from django.views import View 
# from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Project





class Home(TemplateView):
    template_name = "home.html"
class About(TemplateView):
    template_name = "about.html"
class ProjectList(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to access it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["projects"] = Project.objects.filter(name__icontains=name)
        else:
            context["projects"] = Project.objects.all()
        return context