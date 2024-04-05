from rest_framework.views import APIView
from django.http import JsonResponse
from TestFullstack.models import Profile


class Regis(APIView):
    def post(self, *args, **kwargs):
        try:
            data = self.request.data
            print(data)
            prof = Profile()
            prof.name = data['name']
            prof.email = data['email']
            prof.identity_number = data['identity_number']
            prof.birth_of_date = data['date_of_birth']
            print(prof)
            prof.save()
            return JsonResponse(data={
                "message": "Success Insert"
            }, status=200)
        except Exception as e:
            return JsonResponse(data={
                "message": str(e)
            }, status=400)
