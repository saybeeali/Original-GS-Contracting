from django.shortcuts import render
from django.views import View 
# from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Project

class Home(TemplateView):
    template_name = "home.html"
class About(TemplateView):
    template_name = "about.html"
class ProjectList(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["projects"] = Project.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["projects"] = Project.objects.all()
            # default header for not searching 
            context["header"] = f"Searching for {name}"
        return context
class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"
    