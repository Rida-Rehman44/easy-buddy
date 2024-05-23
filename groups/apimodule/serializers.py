from .models import Hunde
from rest_framework import serializers

class HundeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hunde
        fields = '__all__'