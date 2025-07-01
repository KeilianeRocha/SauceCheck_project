import time
import pytest
from tests import conftest
from selenium.webdriver.common.by import By


# Comandos 'assert' → sempre espera um retorno da condição True
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT03:
    def test_ct03_add_prod_carrinho(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        homepage = driver.find_element(By.XPATH, "//*[@class='app_logo']")
        print(homepage.text)
        assert homepage.text == "Swag Labs"

        # Selecionar produto

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # visualizar no carro
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        checkproduct = driver.find_element(By. XPATH, "//*[@class='inventory_item_name']")
        print(checkproduct.text)
        assert checkproduct.text == "Sauce Labs Backpack"
time.sleep(3)