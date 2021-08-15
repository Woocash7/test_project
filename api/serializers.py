from rest_framework import serializers


class ExcelFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    columns = serializers.CharField()
    class Meta:
        fields = ['file', 'columns']