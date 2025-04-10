from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

# @login_required
def add_to_cart(request, book_id):
    cart = request.session.get('cart', {})
    book_id = str(book_id)

    if book_id in cart:
        cart[book_id] += 1
    else:
        cart[book_id] = 1

    request.session['cart'] = cart
    return redirect('book_list')

# @login_required
def decrease_cart(request, book_id):
    cart = request.session.get('cart', {})
    book_id = str(book_id)

    if book_id in cart:
        cart[book_id] -= 1
        if cart[book_id] <= 0:
            del cart[book_id]

    request.session['cart'] = cart
    return redirect('cart')

# @login_required
def remove_from_cart(request, book_id):
    cart = request.session.get('cart', {})
    book_id = str(book_id)

    if book_id in cart:
        del cart[book_id]

    request.session['cart'] = cart
    return redirect('cart')

# @login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for book_id, quantity in cart.items():
        book = get_object_or_404(Book, pk=int(book_id))
        item_total = book.price * quantity
        total_price += item_total
        cart_items.append({
            'book': book,
            'quantity': quantity,
            'total': item_total
        })

    return render(request, 'book/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })
