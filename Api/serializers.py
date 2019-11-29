from rest_framework import serializers
from .models import employe

class employeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = employe
        # feilds = ('firstName' ,' lastName')
        # explicit_fields = '__all__'
        # model = Snippet
        fields = ['first_name','last_name','emp_id']
        # fields = ['__all__']
