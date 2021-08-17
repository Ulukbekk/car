from django.shortcuts import render, redirect

from cars.models import Car
from user.forms import UserRegistrationForm
from user.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserRegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'users/register.html', context)


def user_detail(request,pk):
    user = User.objects.filter(id=pk).first()
    print(user)
    car = Car.objects.filter(author=user)
    print(car)
    return render(request, 'users/user_detail.html',
                  context={'user_detail': user, 'car':car})

