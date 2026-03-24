from django.urls import path
from .views import (
    upload_soil_report,
    soil_result,
    soil_history,
    download_soil_pdf,
    delete_soil_report
)

urlpatterns = [
    path('upload/', upload_soil_report, name='upload_soil'),
    path('result/<int:pk>/', soil_result, name='soil_result'),
    path('history/', soil_history, name='soil_history'),
    path('download/<int:pk>/', download_soil_pdf, name='download_soil_pdf'),

    # DELETE REPORT
    path('delete/<int:report_id>/', delete_soil_report, name='delete_soil_report'),
]