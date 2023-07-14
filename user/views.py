from django.http import JsonResponse

def Userview(request):
    
    return JsonResponse(
        {
            'status': 200,
            "message": 'OK'
        }
    )