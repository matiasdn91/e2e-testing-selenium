from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.cart_item_names = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        self.checkout_button = (By.CSS_SELECTOR, '[data-test="checkout"]')

    def get_items(self):
        elements = self.driver.find_elements(*self.cart_item_names)
        return [el.text for el in elements if el.is_displayed()]

    def remove_item(self, product_name):
        # Click en el botón "remove" usando el atributo data-test
        product_id = product_name.lower().replace(" ", "-")
        remove_button = self.driver.find_element(By.CSS_SELECTOR, f'[data-test="remove-{product_id}"]')
        remove_button.click()
        # Espera simple a que el producto desaparezca
        self.wait.until(
            lambda d: all(product_name not in el.text for el in d.find_elements(*self.cart_item_names))
        )

    def proceed_to_checkout(self):
        # Hace click en el botón de checkout.
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()
