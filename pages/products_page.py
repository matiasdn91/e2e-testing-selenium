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
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

