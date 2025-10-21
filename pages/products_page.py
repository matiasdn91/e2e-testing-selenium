from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.cart_badge = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        self.filter_dropdown = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
        self.cart_icon = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')

    def add_product_to_cart(self, product_name):
        # Agrega un producto al carrito por nombre.
        product_id = product_name.lower().replace(" ", "-")
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-test="add-to-cart-{product_id}"]'))
        )
        add_button.click()

    def remove_product_from_cart(self, product_name):
        # Elimina un producto del carrito por nombre.
        product_id = product_name.lower().replace(" ", "-")
        remove_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-test="remove-{product_id}"]'))
        )
        remove_button.click()

    def get_cart_count(self):
        # Devuelve la cantidad de productos en el carrito.
        try:
            badge = self.wait.until(EC.presence_of_element_located(self.cart_badge))
            return int(badge.text)
        except:
            return 0  # Si no hay badge, el carrito está vacío.

    def filter_products(self, criteria):
        # Ordena los productos según el criterio especificado.
        dropdown = self.wait.until(EC.element_to_be_clickable(self.filter_dropdown))
        select = Select(dropdown)

        mapping = {
            "az": "az",
            "za": "za",
            "lohi": "lohi",
            "hilo": "hilo"
        }

        if criteria in mapping:
            select.select_by_value(mapping[criteria])
        else:
            raise ValueError(f"Criterio inválido: {criteria}")

    def go_to_cart(self):
        # Navega al carrito de compras.
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

