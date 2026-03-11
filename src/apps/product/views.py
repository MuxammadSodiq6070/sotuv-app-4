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

    if request.method == "POST":
        image_file = request.FILES.get("image")
        data = request.POST

        product_name = data.get("product_name")
        product_barcode = data.get("product_barcode")
        product_category = data.get("product_category")

        input_price = data.get("input_price") or 0
        current_price = data.get("current_price") or 0
        wholesale_price = data.get("wholesale_price") or 0

        qoldiq = data.get("qoldiq") or 0
        min_qoldiq = data.get("min_qoldiq") or 0

        status = data.get("status")

        # barcode bo'sh bo'lmasligi kerak
        if not product_barcode:
            msg = "Barcode kiritilmadi!"
            return render(request,"products-create.html",{
                "msg":msg,
                "categories":Category.objects.all()
            })

        # barcode unique bo'lishi kerak
        if Product.objects.filter(barcode=product_barcode).exists():
            msg = "Bu barcode allaqachon mavjud!"
            return render(request,"products-create.html",{
                "msg":msg,
                "categories":Category.objects.all()
            })

        try:
            category = Category.objects.get(id=product_category)

            product = Product.objects.create(
                category=category,
                name=product_name,
                image=image_file,
                barcode=product_barcode.strip(),
                input_price=float(input_price),
                current_price=float(current_price),
                wholesale_price=float(wholesale_price),
                qoldiq=int(qoldiq),
                min_qoldiq=int(min_qoldiq),
                is_active=True if status == "on" else False
            )

            print("Yangi mahsulot:", product)

            return redirect("products_page")

        except Category.DoesNotExist:
            msg = "Kategoriya topilmadi!"
            return render(request,"products-create.html",{
                "msg":msg,
                "categories":Category.objects.all()
            })

    categories = Category.objects.all()

    return render(request,"products-create.html",{
        "categories":categories
    })


def barcode_scanner_page(request):
    return render(request,"barcode-scanner.html")