from rest_framework import serializers
from .models import ExtractedText

class ExtractedTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedText
        fields = '__all__'
