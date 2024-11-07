from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from app.models import *
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth import login # type: ignore
from django.contrib.auth import logout as django_logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import *
from django.contrib import messages # type: ignore
from django.db.models import Q # type: ignore




def BASE (request):
    return render (request, 'base.html')

def Home (request):
    sliders = slider.objects.all()
    main_categorys = main_category.objects.all()
    context = {
        'sliders':sliders,
        'main_categorys':main_categorys,
    }
    return render (request, 'main/home.html', context )


#-------------------------------------------------------------------------------------------
#---------------------------------Product Category Page Start-------------------------------

def category_products(request, slug):
    category = get_object_or_404(main_category, slug=slug)
    products = Product.objects.filter(category=category)

    return render(request, 'main/category_detail.html', {
        'category': category,
        'products': products
    })
#----------------------------------Product category Page Ends-------------------------------
#-------------------------------------------------------------------------------------------

def search_view(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query')
    products = None
    
    if query:
        # Use Q objects for combined filtering
        products = Product.objects.filter(
            Q(product_name__icontains=query) | Q(product_info__icontains=query)
        )
        
    context = {
        'form': form,
        'products': products,
    }
    return render(request, 'main/search.html', context)

def about (request):
    return render (request, 'about.html')
  
def order (request):
    return render (request, 'main/order.html')



#-------------------------------------------------------------------------------------------
#--------------------------------------Login Page Start-------------------------------------
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request , user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect ('home')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)  # Debugging: print errors
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    django_logout(request)
    return redirect('home')

#--------------------------------------Login Page Ends--------------------------------------
#-------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------
#--------------------------------------Cart Page Starts-------------------------------------

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total += product.price * quantity
        cart_items.append({
            'id': product.id,
            'product': product,
            'product_name': product.product_name,
            'image': product.image,
            'price':product.price,
            'quantity': quantity,
            'total_price': product.price * quantity,
            'total': total
        })

    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total': total})


#--------------------------------------Cart Page Ends---------------------------------------
#-------------------------------------------------------------------------------------------