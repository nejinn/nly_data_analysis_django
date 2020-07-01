from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from nly_data_analysis.views.get_data_view import urls as get_data_view_urls

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('nly_data_analysis/', include(get_data_view_urls))
]
