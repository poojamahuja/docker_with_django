from rest_framework.views import APIView
from django.http import HttpResponse


class HomeView(APIView):
    def get(self, request, format=None):
        return HttpResponse(
            'Hello, I am configuring Docker with Django Project and configuring CI/CD pipeline with Banch 2')
