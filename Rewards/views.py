from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django import forms
import json

#Lista en memoria para almacenar las compras
purchases = []

#Formulario para validar datos de la compra
class Purchase(forms.Form):
    id = forms.IntegerField()
    amount = forms.FloatField()
    user = forms.CharField()

#Endpoint para registrar una compra
@csrf_exempt
def create_purchase(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON invalido"}, status=400)

        purchase = Purchase(data)

        if purchase.is_valid():
            purchases.append(purchase.cleaned_data)
            return JsonResponse({"message": "Compra registrada exitosamente", "data": purchase.cleaned_data}, status=201)
        else:
            return JsonResponse({"errors": purchase.errors}, status=400)

    return JsonResponse({"error": "Accion no implementada"}, status=405)

#Endpoint para listar compras de un usuario
@api_view(['GET'])
@csrf_exempt
def list_user_purchases(request, user):
    if request.method == 'GET':
        user_purchases = [purchase for purchase in purchases if purchase['user'] == user]
        return JsonResponse({"data": user_purchases}, status=200)

    return JsonResponse({"error": "Accion no implementada"}, status=405)

#Endpoint para calcular puntos de recompensa
@api_view(['GET'])
@csrf_exempt
def calculate_rewards(request, user):
    if request.method == 'GET':
        #Sumar los montos de las compras del usuario
        total = 0
        for purchase in purchases:
            if purchase["user"] == user:
                total += purchase["amount"]
        reward_points = int(total // 10) 
        return JsonResponse({"user": user, "reward_points": reward_points}, status=200)

    return JsonResponse({"error": "Accion no implementada"}, status=405)