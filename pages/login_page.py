from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.username_input = (By.CSS_SELECTOR, '[data-test="username"]')
        self.password_input = (By.CSS_SELECTOR, '[data-test="password"]')
        self.login_button = (By.CSS_SELECTOR, '[data-test="login-button"]')
        self.error_message = (By.CSS_SELECTOR, '[data-test="error"]')

    def login(self, username, password):
        # Realiza el login con las credenciales provistas.
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()

    def get_error_message(self):
        # Devuelve el mensaje de error si el login falla.
        element = self.wait.until(EC.visibility_of_element_located(self.error_message))
        return element.text
