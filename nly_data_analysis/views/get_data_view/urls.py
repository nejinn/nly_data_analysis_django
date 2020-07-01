from django.urls import path
from nly_data_analysis.views.get_data_view import views

urlpatterns = [
    path('get_return_data/', views.GetReturnExcelFileData.as_view(), name="get_return_data")
]
