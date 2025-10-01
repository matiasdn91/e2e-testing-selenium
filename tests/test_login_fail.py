from pages.login_page import LoginPage

# Test de login con credenciales inválidas.
def test_login_fail(driver):
    login_page = LoginPage(driver)
    login_page.login("invalid_user", "invalid_pass")

    # Forzar un fallo: buscar un elemento que no existe
    assert driver.find_element("id", "non-existent_element")