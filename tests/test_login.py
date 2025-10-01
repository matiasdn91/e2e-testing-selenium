from pages.login_page import LoginPage

# Test de login con credenciales válidas.
def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url