from rest_framework.views import APIView
from rest_framework.response import Response
from nly_data_analysis_django.status import RenderStatus


class GetReturnExcelFileData(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request):

        data = request.FILES.get('excelFile')

        if data is None:
            print(1)
        else:
            print(2)

        print(data)

        data = {
            'go': 1
        }
        return Response(data)
