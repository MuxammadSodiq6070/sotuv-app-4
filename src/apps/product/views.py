from django.shortcuts import render, redirect
from .models import Category, Product
from django.http import JsonResponse
# Create your views here.


def monitoring_page(request):
    return render(request, "monitoring.html")


def products_page(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    
    # Boshlang'ich QuerySet
    products = Product.objects.all()

    # Agar kategoriya tanlangan bo'lsa va u 'all' bo'lmasa filtrlaymiz
    if category_id and category_id != 'all':
        products = products.filter(category_id=category_id)

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products.html', context)

from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages

def products_create_page(request):
    scanned_barcode = request.GET.get('barcode', '')
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        image_file = request.FILES.get("image")

        # Formadan ma'lumotlarni olish
        product_name = data.get("product_name")
        product_barcode = data.get("product_barcode")
        category_id = data.get("product_category")
        
        # Narxlar va miqdorlar (raqam bo'lmasa 0 deb oladi)
        input_price = data.get("input_price") or 0
        current_price = data.get("current_price") or 0
        wholesale_price = data.get("wholesale_price") or 0
        qoldiq = data.get("qoldiq") or 0
        min_qoldiq = data.get("min_qoldiq") or 0
        
        # Status (checkbox 'on' bo'lib keladi)
        is_active = True if data.get("status") == "on" else False

        # 1. Barcode tekshiruvi
        if not product_barcode:
            return render(request, "products-create.html", {
                "msg": "Barcode kiritilmadi!",
                "categories": categories,
                "scanned_barcode": product_barcode
            })

        try:
            # 2. Kategoriyani olish
            category_obj = Category.objects.get(id=category_id)

            # 3. MAHSULOTNI YARATISH (Asosiy qism)
            new_product = Product.objects.create(
                category=category_obj,
                name=product_name,
                image=image_file,
                barcode=product_barcode,
                input_price=input_price,
                current_price=current_price,
                wholesale_price=wholesale_price,
                qoldiq=qoldiq,
                min_qoldiq=min_qoldiq,
                is_active=is_active
            )
            
            # Muvaffaqiyatli saqlangach, ro'yxat sahifasiga o'tish
            messages.success(request, "Mahsulot muvaffaqiyatli yaratildi!")
            return redirect("products_page") # O'zingizning ro'yxat URL nomingizni qo'ying

        except Category.DoesNotExist:
            return render(request, "products-create.html", {
                "msg": "Kategoriya xato tanlandi!",
                "categories": categories
            })
        except Exception as e:
            # Boshqa kutilmagan xatolarni ko'rsatish
            return render(request, "products-create.html", {
                "msg": f"Xatolik yuz berdi: {str(e)}",
                "categories": categories
            })

    return render(request, "products-create.html", {
        "categories": categories,
        "scanned_barcode": scanned_barcode
    })


def barcode(request):
    return render(request,"barcode_scanner.html")




def get_product_by_barcode(request):
    barcode = request.GET.get('barcode')
    try:
        product = Product.objects.get(barcode=barcode, is_active=True)
        return JsonResponse({
            "status": "success",
            "id": product.id,
            "name": product.name,
            "price": float(product.current_price),
            "image": product.image.url if product.image else None
        })
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Mahsulot topilmadi"}, status=404)
    


def pos_sale_view(request):
    barcode = request.GET.get('barcode')
    
    # 1. Agar so'rovda barcode bo'lsa (Skaner so'rov yuborgan bo'lsa)
    if barcode:
        try:
            product = Product.objects.get(barcode=barcode, is_active=True)
            return JsonResponse({
                "status": "success",
                "id": product.id,
                "name": product.name,
                "price": float(product.current_price),
                "image": product.image.url if product.image else None
            })
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Mahsulot topilmadi"}, status=404)
    
    # 2. Agar barcode bo'lmasa (Foydalanuvchi sahifaga kirsa)
    return render(request, "pos_sale.html")