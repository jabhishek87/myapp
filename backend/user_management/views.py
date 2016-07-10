from django.http import JsonResponse, HttpResponse
#from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework import permissions
from . import models
from . import serializers

from rest_framework import renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class PostList(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class APIRoot(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        # Assuming we have views named 'foo-view' and 'bar-view'
        # in our project's URLconf.
        return Response({
            'post-list': reverse('post-list', request=request),
        })