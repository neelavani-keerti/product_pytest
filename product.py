def product_details(name, pro_id, qty, price):
    result = (
        f"Product Name: {name}\n"
        f"Product ID: {pro_id}\n"
        f"Quantity: {qty}\n"
        f"Price: {price}\n"
    )
    return result

if __name__ == "__main__":
    name = "KitKat"
    pro_id = "K193"
    qty = "40g"
    price = 20

    print(product_details(name, pro_id, qty, price))

