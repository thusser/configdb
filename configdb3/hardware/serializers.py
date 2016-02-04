from rest_framework import serializers
from .models import (Site, Enclosure, Telescope,
                     Instrument, Camera, Mode,
                     FilterWheel, CameraType, Filter)


class FilterWheelSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'filters', '__str__')
        model = FilterWheel
        depth = 1


class FilterSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'code', 'filter_type')
        model = Filter
        depth = 1


class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'binning', 'overhead')
        model = Mode


class CameraTypeSerializer(serializers.ModelSerializer):
    default_mode = ModeSerializer()
    mode_set = ModeSerializer(many=True)

    class Meta:
        fields = ('id', 'size', 'pscale', 'default_mode', 'name', 'code', 'mode_set')
        model = CameraType


class CameraSerializer(serializers.ModelSerializer):
    camera_type = CameraTypeSerializer()

    class Meta:
        fields = ('id', 'code', 'camera_type', 'filter_wheel', 'filters')
        model = Camera


class InstrumentSerializer(serializers.ModelSerializer):
    science_camera = CameraSerializer()
    autoguider_camera = CameraSerializer()

    class Meta:
        fields = ('id', 'schedulable', 'telescope', 'science_camera',
                  'autoguider_camera', '__str__')
        model = Instrument


class TelescopeSerializer(serializers.ModelSerializer):
    instrument_set = InstrumentSerializer(many=True)

    class Meta:
        fields = ('id', 'name', 'code', 'active', 'lat',
                  'long', 'enclosure', 'instrument_set', '__str__')
        model = Telescope


class EnclosureSerializer(serializers.ModelSerializer):
    telescope_set = TelescopeSerializer(many=True)

    class Meta:
        fields = ('id', 'name', 'code', 'active', 'site',
                  'telescope_set', '__str__')
        model = Enclosure


class SiteSerializer(serializers.ModelSerializer):
    enclosure_set = EnclosureSerializer(many=True)

    class Meta:
        fields = ('id', 'name', 'code', 'active', 'timezone',
                  'elevation', 'enclosure_set', '__str__')
        model = Site
