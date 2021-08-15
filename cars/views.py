from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cars.forms import CarAddForm, CarUpdateForm
from cars.models import Car


def home_page(request):
    cars = Car.objects.filter().order_by('-date_created')
    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'cars':page_obj,

    }
    return render(request, 'cars/home.html', context)

@login_required
def create_add(request):
    if request.method == 'POST':
        form = CarAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_page')

    form = CarAddForm()
    context = {
        'form': form
    }
    return render(request, 'cars/car_add.html', context)


def car_detail(request, pk):
    car = Car.objects.filter(id=pk)
    cars = Car.objects.all()
    return render(request, 'cars/car_detail.html',
                  context={'car': car, 'cars':cars})
@login_required
def user_car(request):
    car = Car.objects.filter(author=request.user)
    context = {
        'user_car': car,

    }
    return render(request, 'users/user_post.html',
                  context)



def car_update(request, pk):
    car = Car.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = CarUpdateForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = CarUpdateForm(instance=car)
    return render(request, 'cars/car_update.html',
                  context={'car': car, 'form': form})

def car_delete(request, pk):
    car = Car.objects.filter(id=pk).first()
    car.delete()
    return redirect('/')

def search(request):
    query = request.GET.get('q')
    cars = Car.objects.filter(title__icontains=query)
    return render(request, 'cars/home.html',
                  context={'cars': cars})