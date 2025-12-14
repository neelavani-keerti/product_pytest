from product import product_details

def test_product_details():
    expected_output = (
        "Product Name:KitKat\n"
        "Product ID:K193\n"
        "Quantity:40g\n"
        "Price:20\n"
    )
    assert product_details("KitKat", "K193", "40g", 20) == expected_output

