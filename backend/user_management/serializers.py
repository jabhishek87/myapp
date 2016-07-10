from rest_framework import serializers

from . import models


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Post
