import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_product_to_cart(driver):
    # Agrega un producto al carrito y valida que se muestre correctamente.
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    product_name = "Sauce Labs Backpack"

    products_page.add_product_to_cart(product_name)
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    items = cart_page.get_items()

    assert product_name in items
    assert len(items) == 1

def test_remove_product_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    product_name = "Sauce Labs Bike Light"

    products_page.add_product_to_cart(product_name)
    products_page.go_to_cart()

    cart_page = CartPage(driver)

    # Validar que esté en el carrito
    assert product_name in cart_page.get_items()

    # Remover y validar que ya no esté
    cart_page.remove_item(product_name)
    assert product_name not in cart_page.get_items()

def test_filter_products(driver):
    # Valida que se puedan ordenar productos por nombre o precio.
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)

    # Filtra productos A-Z.
    products_page.filter_products("az")

    # Filtra productos Precio Low-High.
    products_page.filter_products("lohi")
