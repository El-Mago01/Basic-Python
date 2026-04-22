VAT_TAX = 11.5 #VAT TAX is 11.5%

def dollar_to_int(dollar):
    dollar_split = dollar.split("$")
    return int(dollar_split[0])  #The dollar sign is expected at the end. E.g. 20$

def get_price_and_amount_received():
     product_price_str = input("Enter product price: ")
     amount_received_from_customer_str = input("Enter amount received_from_customer: ")
     product_price=dollar_to_int(product_price_str)
     amount_received_from_customer=dollar_to_int(amount_received_from_customer_str)
     return product_price, amount_received_from_customer

def calculate_price_with_tax_and_change(price_without_tax, amount_received_from_customer):
    price_with_tax = price_without_tax  * ((100+VAT_TAX)/100)
    change= amount_received_from_customer - price_with_tax
    return price_with_tax, change

def main():
    price_without_tax , amount_received=get_price_and_amount_received()
    product_price_with_tax,change = calculate_price_with_tax_and_change(price_without_tax, amount_received)
    print(f"The product_price_with_tax is: {product_price_with_tax}")
    print(f"The change to give back to customer is: {change}")

if __name__ == "__main__":
    main()