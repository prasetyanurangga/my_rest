from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from note.models import NoteModel
from note.serializers import NoteSerializer

@csrf_exempt
@api_view(['GET','POST'])
def note_list(request, format=None):
	if request.method == "GET":
		note = NoteModel.objects.all()
		seria = NoteSerializer(note, many=True)
		return Response(seria.data)

	elif request.method == "POST":
		data = JSONParser().parse(request)
		seria = NoteSerializer(data=data)
		if seria.is_valid():
			seria.save()
			return Response(seria.data, status=status.HTTP_201_CREATED)
		return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)	
# Create your views here.
