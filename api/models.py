from django.db import models

def excel_files_path(instance, filename):
    return f'excel_files/{filename}'

# Create your models here.
class ExcelFile(models.Model):
    file = models.FileField(upload_to=excel_files_path)

    def __str__(self):
        return f'{self.file.name}'

    @property
    def filename(self):
        return f'{self.file.name.split("/")[-1]}'