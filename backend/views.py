from django.http import JsonResponse, request
from django.shortcuts import render

# third party imports .
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializers import EventSerializer
from.models import Event
from django.db.migrations import serializer


class TestApi(APIView):
    def get(self, request, *args, **kwargs):
        qs = Event.objects.all()
        #event = qs.first()
        serializer = EventSerializer(qs, many=True)
        return Response(serializer.data)



    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# sample json resonse data 
# def test_api(request):
#      data = {
#         'title': ' Heading for the best',
#         'description':' we are live now no shaking ',
#         'locaction ':'wembley park',
#         'date': 'December'
#      }
#      return JsonResponse(data)