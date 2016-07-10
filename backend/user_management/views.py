from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from rest_framework import mixins

from . import models
from . import serializers

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


class SignUpViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    permission_classes = (permissions.AllowAny,) # Or anon users can't register
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
