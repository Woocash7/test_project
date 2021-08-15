import pandas as pd

from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status

from api.models import ExcelFile
from api.serializers import ExcelFileSerializer

class ExcelFileCreate(CreateAPIView):
    serializer_class = ExcelFileSerializer

    def create(self, request, *args, **kwargs):
        excel_file = ExcelFile.objects.create(
            file=request.data['file']
        )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        columns = [column.strip() for column in serializer.data['columns'].split(',')]
        df = pd.read_excel(excel_file.file.path)
  
        try:
            summary = [{'column': column, 'sum': df[column].sum(), 'avg': df[column].mean()} for column in columns]
            return Response(
            {
                'filename': excel_file.filename,
                'summary': summary
            },
            status=status.HTTP_201_CREATED
        )
        except KeyError:
            return Response('Invalid column name', status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response('Required numerical data', status=status.HTTP_400_BAD_REQUEST)
