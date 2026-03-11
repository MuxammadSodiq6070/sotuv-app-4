from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.





def dashboard_page(request):
    if not request.user.is_authenticated:
        return redirect("login_page")
    
    return render(request,'dashboard.html')



def login_page(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        msg = "login yoki Parol Xato!"
    contex = {"msg" : msg}
    return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect("login_page")