from django.db import models
from django.conf import settings

class SoilReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ph = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    organic_carbon = models.FloatField()

    crop_recommendation = models.CharField(max_length=255, blank=True, null=True)
    fertilizer_advice = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Soil Report - {self.user.username}"