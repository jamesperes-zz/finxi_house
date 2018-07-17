from django.shortcuts import render, redirect, get_object_or_404
from .models import House, Customer, Seller, Image
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.forms import modelformset_factory
from django.db.models import Q

import geocoder
from geopy.distance import vincenty

from .forms import UserForm, HouseForm


def home(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    houses_home = House.objects.all()
    context = {"houses_home": houses_home, "user": user}
    return render(request, "finxi_web/home.html", context)


def create_customer(request):
    error_list = []
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            customer_user = form.save()
            customer_user.set_password(customer_user.password)
            customer = Customer.objects.create(user=customer_user)
            messages.success(request, "Usuario criado com sucesso!")
            return redirect("home")
        else:
            error_list = form.errors
    else:
        form = UserForm()
    context = {"form": form, "error_list": error_list}
    return render(request, "registration/create_customer.html", context)


@staff_member_required
def create_seller(request):
    """View create Seller

    For staff members only
    """
    error_list = []
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            seller_user = form.save()
            seller_user.set_password(seller_user.password)
            seller = Seller.objects.create(user=seller_user)
            messages.success(request, "vendedor criado com sucesso!")
            return redirect("home")

        else:
            error_list = form.errors
    else:
        form = UserForm()
    context = {"form": form, "error_list": error_list}
    return render(request, "registration/create_seller.html", context)


@staff_member_required
def create_house(request):
    """View create House

    For staff members only
    """
    error_list = []
    ImageFormset = modelformset_factory(Image, fields=("image_file",), extra=2)
    if request.method == "POST":
        form = HouseForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            house_values = form.save(commit=False)
            current_user = request.user
            seller = Seller.objects.filter(user__id=current_user.id)[0]
            house_values.seller = seller
            house_values.save()
            for f in formset:
                try:
                    photo = Image(
                        house=house_values, image_file=f.cleaned_data["image_file"]
                    )
                    photo.save()
                except Exception as e:
                    break

            messages.success(request, "Anuncio criado com sucesso!")
            return redirect("home")
        else:
            error_list = form.errors
    else:
        form = HouseForm()
        formset = ImageFormset(queryset=Image.objects.none())

    context = {"form": form, "formset": formset, "error_list": error_list}
    return render(request, "registration/create_house.html", context)


def house_detail(request, house_id):
    """View get House detail"""
    house = get_object_or_404(House, id=house_id)
    houses = House.objects.exclude(id=house_id)
    house_position = (house.lat, house.lng)
    houses_near_result = []
    for house_near in houses:
        distance = vincenty(house_position, (house_near.lat, house_near.lng)).kilometers
        if distance <= 10.0:
            houses_near_result.append(house_near)
    context = {"house": house, "houses_near_result": houses_near_result}
    return render(request, "finxi_web/house.html", context)


def search(request):
    """View get House list"""
    houses = House.objects.all()
    search = request.POST.get("search")
    result = houses.filter(Q(district__icontains=search) | Q(street__icontains=search))
    search_position = geocoder.google(search)

    if None in (search_position.lat, search_position.lng):
        return render(request, "finxi_web/search.html", {"result": result})

    center_search = (str(search_position.lat), str(search_position.lng))

    houses_near = []
    for house in houses:
        if None not in (house.lat, house.lng):
            distance = vincenty(center_search, (house.lat, house.lng)).kilometers
            if distance <= 10.0:
                houses_near.append(house)
    context = {"result": result, "houses_near": houses_near}
    return render(request, "finxi_web/search.html", context)
