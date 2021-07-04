from django.shortcuts import HttpResponse
from . models import ShipData
import csv


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . serializers import ShipSerializer, ShipDataSerializer


# Create your views here.
@api_view(["GET"])
def ships_list(request):

    if request.method == "GET":
        ships = ShipData.objects.order_by().values('name', 'imoNumber').distinct()
        serializer = ShipSerializer(ships, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def ship_detail_view(request, imo):
    try:
        ship_data = ShipData.objects.filter(imoNumber=imo)
    except ShipData.DoesNotExist:
        return Response({"error": {
            "code": 404,
            "message": "game not found",
        }
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ShipDataSerializer(ship_data, many=True)
        return Response(serializer.data)


# load data to database
def load_csv(request):
    ships_mapping = {
        "9632179": "Mathilde Maersk",
        "9247455": "Australian Spirit",
        "9595321": "MSC Preziosa"
    }

    with open('positions.csv', newline='') as file:
        reader = csv.reader(file, delimiter=',')

        # store the headers in a separate variable,
        # move the reader object to point on the next row
        # headings = next(reader)

        # output list to store all rows
        Output = []
        for row in reader:
            Output.append(row[:])

    for rows in range(len(Output)):
        ship_data = ShipData(
            name=ships_mapping[Output[rows][0]],
            imoNumber=Output[rows][0],
            time_stamp=Output[rows][1][0:19],
            latitude=Output[rows][2],
            longitude=Output[rows][3]
        )
        ship_data.save()

    return HttpResponse("data loaded")
