from django.http import JsonResponse
from .models import Order, OrderItem
from apps.product.models import Product
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.product.models import Product
from django.shortcuts import redirect, render
from apps.customer.models import Customer
import json









def sotuv_page(request):
    customers = Customer.objects.all()
    selected_customer = request.GET.get("customer",None)
    context = {
        "customers" : customers,
        "selected_customer":selected_customer
    }
    # if request.method == "POST":
    #     data = json.loads(request.body)
    #     items = data.get('items', [])
        
    #     if not items:
    #         return JsonResponse({"status": "error", "message": "Savat bo'sh"}, status=400)

    #     # 1. Order yaratish
    #     order = Order.objects.create(
    #         total_price=data.get('total_amount'),
    #         payment_type=data.get('payment_type', 'cash')
    #     )

    #     # 2. Mahsulotlarni birma-bir OrderItem-ga qo'shish va qoldiqni kamaytirish
    #     for item in items:
    #         product = Product.objects.get(id=item['id'])
    #         OrderItem.objects.create(
    #             order=order,
    #             product=product,
    #             quantity=item['qty'],
    #             price=item['price']
    #         )
    #         # Ombordagi qoldiqni kamaytiramiz
    #         product.qoldiq -= int(item['qty'])
    #         product.save()

    #     return JsonResponse({"status": "success", "order_id": order.id})
    return render(request,'sotuv.html', context=context)





