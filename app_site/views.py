from django.shortcuts import render,redirect
from app_products.models import Product
from app_users.forms import CustomerForm
# home page
def index(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            customer_form = CustomerForm(request.POST)
            return render(request,'app_site/index.html',{'customer_form':customer_form})
    else:
        customer_form = CustomerForm()
        products = Product.objects.all()
        context = {'products':products,'customer_form':customer_form}
        try:
            
            return render(request,'app_site/index.html',context)
        except:
            return render(request, '404.html')