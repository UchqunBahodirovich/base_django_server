from rest_framework import serializers
from main_app import models


# class ConferenceSerializer(serializers.ModelSerializer):
#     scientist = ScientistSerializer(many=True, read_only=True)

#     class Meta:
#         model = Author
#         fields = ('id', 'conference_name', 'country','city','year', 'scientist')

class ScientistSerializer(serializers.ModelSerializer):
    
    conferences = serializers.StringRelatedField(many=True)
    research_link = serializers.StringRelatedField(many=True)

    class Meta:
    	model = models.Scientist
    	fields = ["id","full_name","degree","specialization","email","research_topics","image","conferences","research_link"]
        

class ScientistNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Scientist
		fields = ["id","full_name","degree","specialization","email","research_topics"]