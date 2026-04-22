def apply_discount( product_price, discount_percentage):
    return f"The new price is {product_price-(product_price * discount_percentage/100)}"

print(apply_discount(100,10))