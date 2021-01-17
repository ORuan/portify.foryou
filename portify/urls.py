from django.urls import path, include
from portify.views import portify_create

urlpatterns = [
    path('create/', portify_create, name='portify')
]