from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'post', views.PostList)


urlpatterns = [
    url(r'^$', views.APIRoot.as_view()),
    url(r'^', include(router.urls)),
]