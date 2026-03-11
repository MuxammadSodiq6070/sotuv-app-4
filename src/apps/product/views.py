from django.shortcuts import render, redirect
from .models import Category, Product
# Create your views here.


def monitoring_page(request):
    return render(request, "monitoring.html")


def products_page(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "products.html", context=context)

def products_create_page(request):
    # URL orqali kelgan barcodeni olish (GET so'rovi orqali)
    scanned_barcode = request.GET.get('barcode', '')

    if request.method == "POST":
        image_file = request.FILES.get("image")
        data = request.POST

        product_name = data.get("product_name")
        product_barcode = data.get("product_barcode")
        product_category = data.get("product_category")

        # ... (qolgan barcha kodlaringiz o'zgarishsiz qoladi) ...
        
        # Barcode bo'sh bo'lmasligi kerak qismi
        if not product_barcode:
            msg = "Barcode kiritilmadi!"
            return render(request, "products-create.html", {
                "msg": msg,
                "categories": Category.objects.all(),
                "scanned_barcode": product_barcode # Xato bo'lsa formadagi qiymatni qaytaramiz
            })
            
        # ... (Product.objects.create qismi va h.k.) ...

    categories = Category.objects.all()
    return render(request, "products-create.html", {
        "categories": categories,
        "scanned_barcode": scanned_barcode  # Skanerdan kelgan kodni templatega uzatamiz
    })
def barcode(request):
    return render(request,"barcode_scanner.html")