from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Project, Category

class HomeView(ListView):
    template_name = "templates/portfolio.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.select_related("category").all()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context