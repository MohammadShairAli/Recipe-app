from django.shortcuts import render, redirect
from .models import recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.utils.crypto import get_random_string

def posted_recipe(request):
    pass


@login_required(login_url='/login/')
def getting_recipe(request):

    if request.method == 'POST':
        messages.success(request,'LogIn successfully')
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_discription = data.get('recipe_discription')
        recipe_image = request.FILES.get('recipe_image')
        new_recipe = recipe.objects.create(user = request.user,recipe_name = recipe_name, recipe_discription = recipe_discription, recipe_image = recipe_image)
        if new_recipe:
            messages.success(request,'Recipe uploaded successfully')
        else:
            messages.error(request,'Failed to upload recipe')
        context = {'user':request.user}
        return redirect('/recipe/')

    search = request.GET.get('search','')

    if search:
        recipes = recipe.objects.filter(user=request.user).filter(recipe_name__icontains = request.GET.get('search'))    
        if recipes.exists():
            messages.success(request,'Products Found successfully')
        else:
            messages.error(request,'Product does not exists')
    else:
        recipes = recipe.objects.filter(user=request.user)
        # recipes = recipe.objects.all()
    
    
    context = {'recipes':recipes,'search':search}
    return render(request,'getting_recipe.html',context)

def delete(request,id):
    deleting = recipe.objects.filter(id = id).first()
    deleting.delete()
    messages.success(request,'Recipe deleted successfully')
    return redirect('/recipe/')


def update(request,id):
    update = recipe.objects.filter(id = id).first()

    if request.method == 'POST':
        data = request.POST
        
        if data.get('recipe_name'):
            update.recipe_name = data.get('recipe_name')

        if data.get('recipe_discription'):
            update.recipe_discription = data.get('recipe_discription')

        if request.FILES.get('recipe_image'):
            update.recipe_image = request.FILES.get('recipe_image')
        
        update.save()
        messages.success(request, 'Recipe Updated successfully')
        return redirect('/recipe/')

    context = {'update':update}
    return render(request,'updating_recipe.html',context)


def signup(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name','')
        last_name = data.get('last_name','')
        email = data.get('email','')
        password1 = data.get('password1','')
        password2 = data.get('password2','')

        if password1 != password2:
            messages.error(request,'Password do not match')
            return redirect('/signup/')

        if User.objects.filter(email = email).exists():
            messages.error(request, "email already exists")
            return redirect('/signup/')

        user = User.objects.create(first_name = first_name,last_name=last_name,username=email)
        user.set_password(password1)
        user.save()

        messages.success(request, "User created successfully")
        
        return redirect('/login/')
    return render(request, 'signup.html')
    
def logout_page(request):
    logout(request)
    return redirect('/login/')

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email','')
        password = data.get('password','')

        user = authenticate(username=email, password=password)
        if user:
            messages.success(request,'You login successfully')
            login(request, user)
            return redirect('/recipe/')
        else:
            messages.error(request,'Incorrect credentials')
            return redirect('/login/')

    return render(request,'login.html')

def Reset_password(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        user = User.objects.filter(username=email).first()
        if user:
            name = user.first_name
            password = get_random_string(length=8, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()')
            print(password)
            user.set_password(password)
            user.save()
            subject = "Your New Password for Recipe App"
            message = f"Dear {name},\n\nWe wanted to let you know that your new password has been successfully created for your Recipe App account.\n\nNew password: {password}\n\nPlease keep this password secure. If you didn't request this change or have any concerns, don't hesitate to reach out to our support team.\n\nThank you for using Recipe App. We're here to help you find the best Recipe deals!\n\nBest regards,\nThe Recipe App Team"
            from_email = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, from_email, [email])
            messages.success(request, 'Password Sent successfully')
            return render(request, 'login.html')
        else:
            messages.error(request,"Email doesn't exist")

    return render(request, 'reset_password.html')
