from django.urls import path
from blog import views

urlpatterns = [
    path('', view=views.blogIndex, name="Blog Homepage")
]