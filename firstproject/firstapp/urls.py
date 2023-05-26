from django.urls import path
from firstapp import views

urlpatterns=[
    path('wish/',views.wish),
    path('hello/',views.hello_view),
    path('person/',views.listview),
]