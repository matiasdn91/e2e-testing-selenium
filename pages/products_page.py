from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver

class ProductsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Localizadores
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT_ADD_BUTTON = "//div[text()='{}']/ancestor::div[@class='inventory_item']//button"
    PRODUCT_REMOVE_BUTTON = "//div[text()='{}']/ancestor::div[@class='inventory_item']//button"
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    # Agrega un producto al carrito por su nombre.
    def add_product_to_cart(self, product_name: str):
        button_xpath = self.PRODUCT_ADD_BUTTON.format(product_name)
        add_button = self.driver.find_element(By.XPATH, button_xpath)
        add_button.click()

    # Elimina un producto del carrito por su nombre.
    def remove_product_from_cart(self, product_name: str):
        button_xpath = self.PRODUCT_REMOVE_BUTTON.format(product_name)
        remove_button = self.driver.find_element(By.XPATH, button_xpath)
        remove_button.click()

    # Devuelve la cantidad de productos en el carrito.
    def get_cart_count(self) -> int:
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except:
            return 0  # Si no hay badge, el carrito está vacío

    # Filtra/ordena productos por criterio
    def filter_products(self, criteria: str):
        dropdown = self.driver.find_element(*self.FILTER_DROPDOWN)
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
