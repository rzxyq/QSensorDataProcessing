from django.conf.urls import url, include
from .views import *

urlpatterns = [
        url(r'^results', Results.as_view()),
        url(r'^result_view',ResultView.as_view()), # To receive 
        url(r'^post_data', post_data), # To receive data POSTs 
        url(r'^post_graph', post_graph), # To receive graph POSTs
]