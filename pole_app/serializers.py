from rest_framework import serializers
from . models import *


class ShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShipData
        # fields = "__all__" # we want all fields in the model
        fields = ("name", "imoNumber") # we want to choose couple of fields
        #exclude = ("id",)


class ShipDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShipData
        # fields = "__all__" # we want all fields in the model
        # fields = ("name", "imoNumber") # we want to choose couple of fields
        exclude = ("id",)


