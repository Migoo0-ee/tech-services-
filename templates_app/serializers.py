# serializer => convert model data into json to be read in flutter 

# templates/serializers.py
from rest_framework import serializers
from .models import Templates

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Templates
        fields = '__all__'  


'''

  Explaination of the code 

  serializers.ModelSerializer --> the method convert data into json, supported by Django rest API
  model = Templates  --> we use data base of templates 
  fields = '__all__'   --> convert all fields into json 

'''