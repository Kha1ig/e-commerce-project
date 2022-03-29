from django.urls import path
from Pages.views import track

app_name = 'track'

urlpatterns = [
    path('', track, name='track'),

]