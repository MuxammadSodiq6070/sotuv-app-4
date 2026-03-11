import json
from django.http import JsonResponse
from .models import Order, OrderItem
from apps.product.models import Product
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.product.models import Product
from .models import Order, OrderItem

def make_sale_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            items = data.get('items', [])
            total_amount = data.get('total_amount')
            payment_type = data.get('payment_type', 'cash')

            if not items:
                return JsonResponse({"status": "error", "message": "Savat bo'sh!"}, status=400)

            # 1. Order (Sotuv) yaratish
            order = Order.objects.create(
                total_price=total_amount,
                payment_type=payment_type
            )

            # 2. Savatdagi har bir mahsulotni aylanib chiqish
            for item in items:
                product = Product.objects.get(id=item['id'])
                
                # OrderItem yaratish
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['qty'],
                    price=item['price']
                )

                # Mahsulot qoldig'ini kamaytirish
                product.qoldiq -= int(item['qty'])
                product.save()

            return JsonResponse({
                "status": "success", 
                "message": "Sotuv muvaffaqiyatli yakunlandi",
                "order_id": order.id
            })

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
    return JsonResponse({"status": "error", "message": "Faqat POST so'rovi qabul qilinadi"}, status=405)


def make_sale(request):
    if request.method == "POST":
        data = json.loads(request.body)
        items = data.get('items', [])
        
        if not items:
            return JsonResponse({"status": "error", "message": "Savat bo'sh"}, status=400)

        # 1. Order yaratish
        order = Order.objects.create(
            total_price=data.get('total_amount'),
            payment_type=data.get('payment_type', 'cash')
        )

        # 2. Mahsulotlarni birma-bir OrderItem-ga qo'shish va qoldiqni kamaytirish
        for item in items:
            product = Product.objects.get(id=item['id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['qty'],
                price=item['price']
            )
            # Ombordagi qoldiqni kamaytiramiz
            product.qoldiq -= int(item['qty'])
            product.save()

        return JsonResponse({"status": "success", "order_id": order.id})