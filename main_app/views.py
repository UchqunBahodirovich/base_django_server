from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from main_app.models import Scientist

from main_app.serializers import ScientistNameSerializer,ScientistSerializer

# Create your views here.
class GetAllScientistName(APIView):
	def get(self, request):
		scientist = Scientist.objects.all()
		serializer_for_queryset = ScientistNameSerializer(scientist,many=True)
		return Response(serializer_for_queryset.data)

class GetByScientistName(APIView):
	def get(self, request,full_name):
		print(request.data)
		queryset = get_object_or_404(Scientist.objects.all(),full_name=full_name)
		print(queryset.degree)
		serializer_for_queryset = ScientistSerializer(queryset)
		return Response(serializer_for_queryset.data)

class GetByScientistId(APIView):
	def get(self, request,id):
		print(request.data)
		queryset = get_object_or_404(Scientist.objects.all(),id=id)
		print(queryset.degree)
		serializer_for_queryset = ScientistSerializer(queryset)
		return Response(serializer_for_queryset.data)