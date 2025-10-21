from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)
    inventory_title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".title"))
    )

    # Validar que el título de la página sea "Products".
    assert inventory_title.text == "Products", \
        f"Título inesperado después del login: {inventory_title.text}"
