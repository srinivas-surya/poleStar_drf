from django.urls import path
from . views import load_csv, ships_list, ship_detail_view

urlpatterns = [

    path('load_csv/', load_csv, name="load_csv"),
    path("ships/",
         ships_list,
         name="ship-list"),
    path("positions/<str:imo>/",ship_detail_view,name="ship-detail"),
]