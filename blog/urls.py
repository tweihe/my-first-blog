from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.english_project, name='english_project'),
]
