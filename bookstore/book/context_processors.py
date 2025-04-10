def cart_item_count(request):
    cart = request.session.get('cart', {})
    if isinstance(cart, dict):
        count = sum(cart.values())
    else:
        count = 0  # Fallback in case cart is not a dict
    return {'cart_item_count': count}
