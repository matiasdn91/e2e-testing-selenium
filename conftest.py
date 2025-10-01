import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from datetime import datetime
import time

# Carpeta para guardar screenshots de los tests fallidos
SCREENSHOT_DIR = os.path.join("reports", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture
def driver(request):
    # Leemos la variable de entorno BROWSER para elegir navegador
    browser = os.environ.get("BROWSER", "chrome").lower()

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Navegador no soportado: {browser}")

    # Maximizar y minimizar para asegurarnos de que se vea la ventana en escritorio
    driver.minimize_window()
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")

    yield driver

    # Teardown: si el test falló, guardamos un screenshot
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_file = os.path.join(
            SCREENSHOT_DIR, f"{test_name}_{browser}_{timestamp}.png"
        )
        driver.save_screenshot(screenshot_file)
        print(f"\n[Screenshot guardado] {screenshot_file}")

    time.sleep(2)
    driver.quit()

# Hook que permite identificar si el test falló
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
