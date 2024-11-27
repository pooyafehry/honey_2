# categorylist/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta

from .forms import CategoryForm, CommentForm, CartAddForm  # Removed AddressForm
from .models import Category, Cart, CartItem, Comment

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    else:
        return render(request, 'category_confirm_delete.html', {'category': category})

@login_required
def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_list.html', context)

@login_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        cart_count = cart_items.count()
    else:
        cart_items = []
        cart_count = 0

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.category = category
            comment.save()
            return redirect('category_detail', pk=pk)
    else:
        form = CommentForm()

    context = {
        'category': category,
        'cart_count': cart_count,
        'cart_items': cart_items,
        'comments': category.comments.all(),
        'form': form,
    }
    return render(request, 'category_detail.html', context)

@login_required
def add_to_cart(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, category=category)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item.price = category.price
            cart_item.save()

    return redirect('cart_detail')

@login_required
def remove_from_cart(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, category=category)
        
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart_detail')

@login_required
def cart_detail(request):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.price * item.quantity for item in cart_items)
    else:
        cart_items = []
        total_price = 0

    context = {
        'cart_items': cart_items,
        'total_price': total_price  # Include total price in the context
    }
    return render(request, 'cart_detail.html', context)
