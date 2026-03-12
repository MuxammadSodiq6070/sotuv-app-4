from django.shortcuts import render, redirect

# Create your views here.




def customer_create(request):
    print("mijoz yaratildi")
    return redirect("sotuv_page.html")