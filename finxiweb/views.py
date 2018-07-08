from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import House, Customer, Seller
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout



from .forms import UserForm

def home(request):
    houses_home = House.objects.all().order_by('?')[:3]
    template = loader.get_template('finxiweb/home.html')
    context = {houses_home:"houses_home"}
    return HttpResponse(template.render(context, request))


def create_customer(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            customer_user = form.save()
            customer_user.set_password(customer_user.password)
            customer_user.save()
            customer = Customer.objects.create(user=customer_user)
            messages.success(request, 'Usuario criado com sucesso!')
            return redirect('')
    else:
        form = UserForm()
    return render(request, 'registration/create_customer.html', {'form':form})


@staff_member_required
def create_seller(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            seller_user = form.save()
            seller_user.set_password(seller_user.password)
            seller_user.save()
            seller = Seller.objects.create(user=seller_user)
            messages.success(request, 'vendedor criado com sucesso!')
            return redirect('')
    else:
        form = UserForm()
    return render(request, 'registration/create_seller.html', {'form':form})


