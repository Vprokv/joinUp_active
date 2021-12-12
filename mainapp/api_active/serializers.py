from rest_framework import serializers

from ..models import Program


class ProgramSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()

    class Meta:
        model = Program
        fields = '__all__'
