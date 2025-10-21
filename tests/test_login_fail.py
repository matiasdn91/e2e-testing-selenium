from pages.login_page import LoginPage


def test_login_with_invalid_credentials(driver):
    login_page = LoginPage(driver)

    # Login con credenciales incorrectas.
    login_page.login("usuario_invalido", "contraseña_invalida")

    # Validar mensaje de error.
    error_text = login_page.get_error_message()
    expected_text = "Epic sadface: Username and password do not match any user in this service"

    assert error_text == expected_text, f"Mensaje inesperado: {error_text}"

def test_login_with_empty_fields(driver):
    login_page = LoginPage(driver)

    # Login sin ingresar datos.
    login_page.login("", "")

    error_text = login_page.get_error_message()
    expected_text = "Epic sadface: Username is required"

    assert error_text == expected_text, f"Mensaje inesperado: {error_text}"

