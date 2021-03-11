from django.http import JsonResponse

def bares(request):
    if request.method == 'GET':
        bar = {'id': 1, 'nome': 'Garrafeiros'}
        return JsonResponse(bar)
