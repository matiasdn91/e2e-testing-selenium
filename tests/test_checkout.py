import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_successful_checkout(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Agregar producto.
    products_page = ProductsPage(driver)
    product_name = "Sauce Labs Bolt T-Shirt"
    products_page.add_product_to_cart(product_name)
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    items = cart_page.get_items()
    assert product_name in items, "El producto no se agregó correctamente al carrito."

    # Ir a Checkout.
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Matias", "Nazadek", "1234")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    # Validación final.
    message = checkout_page.get_success_message()
    assert message == "Thank you for your order!", "El mensaje de confirmación no coincide."
