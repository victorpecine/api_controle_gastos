from django.http import JsonResponse

def gastos(request):
    if request.method == 'GET':
        gasto = {
                'id_gastos':             1,
                'id_usuario':           'Victor',
                'id_estabelecimento':   'Garrafeiros',
                'id_categoria':         'Bar',
                'valor':                f'{22.50:.2f}',
                'data_gasto':           '2021-02-12',
                'forma_pagamento':      'Debito'
                }
        return JsonResponse(gasto)
