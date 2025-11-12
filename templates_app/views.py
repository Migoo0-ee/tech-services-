from django.shortcuts import render

# Create your views here.
# templates/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Templates
from .serializers import TemplateSerializer

# return all templates
@api_view(['GET'])
def template_list(request):
    templates = Templates.objects.all()
    serializer = TemplateSerializer(templates, many=True)
    return Response(serializer.data)

# filter by category 
@api_view(['GET'])
def template_list_by_category(request, category):
    templates = Templates.objects.filter(category=category)
    serializer = TemplateSerializer(templates, many=True)
    return Response(serializer.data)


# free or paid template 
@api_view(['GET'])
def template_list_free_paid(request, is_paid):
    templates = Templates.objects.filter(is_paid=is_paid)
    serializer = TemplateSerializer(templates, many=True)
    return Response(serializer.data)  # return serializer data 


# serializer = TemplateSerializer(templates, many=True)
# this is our initialized class in serializer.py who convert model data into json 
# many = true --> to fetch all data not one record only 


