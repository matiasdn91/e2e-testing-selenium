from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.first_name_input = (By.CSS_SELECTOR, '[data-test="firstName"]')
        self.last_name_input = (By.CSS_SELECTOR, '[data-test="lastName"]')
        self.postal_code_input = (By.CSS_SELECTOR, '[data-test="postalCode"]')
        self.continue_button = (By.CSS_SELECTOR, '[data-test="continue"]')
        self.finish_button = (By.CSS_SELECTOR, '[data-test="finish"]')
        self.success_message = (By.CSS_SELECTOR, '[data-test="complete-header"]')

    def fill_checkout_form(self, first_name, last_name, postal_code):
        # Completa el formulario con los datos del usuario.
        self.wait.until(EC.presence_of_element_located(self.first_name_input)).send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]').send_keys(postal_code)

    def continue_checkout(self):
        # Hace clic en el botón Continue.
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def finish_checkout(self):
        # Hace clic en el botón Finish.
        self.wait.until(EC.element_to_be_clickable(self.finish_button)).click()

    def get_success_message(self):
        # Devuelve el texto del mensaje de confirmación.
        element = self.wait.until(EC.visibility_of_element_located(self.success_message))
        return element.text
