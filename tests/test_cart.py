import pytest
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
import os

# Agregamos un producto al carrito y validamos que el contador aumente.
def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)

    # Agregar un producto
    product_name = "Sauce Labs Backpack"
    products_page.add_product_to_cart(product_name)

    # Validar que el contador del carrito sea 1
    assert products_page.get_cart_count() == 1

# Agregamos y luego eliminamos un producto del carrito, validamos que el contador vuelva a 0.
def test_remove_product_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    product_name = "Sauce Labs Bike Light"

    # Agregar producto
    products_page.add_product_to_cart(product_name)
    assert products_page.get_cart_count() == 1

    # Eliminar producto
    products_page.remove_product_from_cart(product_name)
    assert products_page.get_cart_count() == 0

# Validamos que se puedan ordenar productos por nombre o precio.
def test_filter_products(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)

    # Filtrar productos A-Z
    products_page.filter_products("az")
    
    # Filtrar productos Precio Low-High
    products_page.filter_products("lohi")
