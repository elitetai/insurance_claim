from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator


class Claim(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    vehicle_manufacture_year = models.CharField(max_length=4)
    vehicle_model = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=8)
    date_and_time_of_accident = models.DateTimeField()
    accident_location = models.CharField(max_length=255)
    type_of_loss = models.CharField(max_length=20)
    description_of_loss = models.TextField(max_length=300)
    police_report_lodged = models.BooleanField()
    anybody_injured = models.BooleanField()
    photo = models.ImageField(upload_to='uploads/')
    document_in_pdf_format = models.FileField(upload_to='files/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    claim_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='claim', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name