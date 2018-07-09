from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import House, Customer, Seller, Image
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.forms import modelformset_factory





from .forms import UserForm, HouseForm

def home(request):
    houses_home = House.objects.all()
    template = loader.get_template('finxiweb/home.html')
    context = {'houses_home':houses_home}
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



def create_house(request):
    ImageFormset = modelformset_factory(Image, fields=('image_file',), extra=4)
    if request.method == 'POST':
        form = HouseForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid() :
            house_values = form.save()
            current_user = request.user
            seller = Seller.objects.filter(user__id=current_user.id)[0]
            house_values.seller = seller
            house_values.save()
            for f in formset:
                try:
                    photo = Image(house=house_values,
                                  image_file=f.cleaned_data['image_file'])
                    photo.save()
                except Exception as e:
                    break

            messages.success(request, 'Anuncio criado com sucesso!')
            return redirect('home')
    else:
        form = HouseForm()
        formset = ImageFormset(queryset=Image.objects.none())

    context = {
        'form':form,
        'formset':formset
    } 
    return render(request, 'registration/create_house.html', context)
