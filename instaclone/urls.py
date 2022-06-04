from operator import index
from django .urls import path

urlpatterns = [
     path('',views.index, name=index)
]