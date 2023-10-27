from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class TestView(APIView):
    def get(self, request, format=None):
        print("API Was Called")
        return Response("You Made It", status=200)