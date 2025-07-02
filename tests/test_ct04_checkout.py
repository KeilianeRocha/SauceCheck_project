import time
import pytest

from pages.login_page import LoginPage
from tests import conftest
from selenium.webdriver.common.by import By


# Comandos 'assert' → sempre espera um retorno da condição True
@pytest.mark.usefixtures("setup_teardown")

class TestCT04:
    def test_ct04_checkout(self):
        driver = conftest.driver
        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_sauce")

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

        # Checkout
        driver.find_element(By.ID, "checkout").click()
        firstName = driver.find_element(By.ID, "first-name").send_keys("Teste")
        lastName = driver.find_element(By.ID, "last-name").send_keys("Lorem")
        zipCode = driver.find_element(By.ID, "postal-code").send_keys("12345-010")
        continue_button = driver.find_element(By.ID, "continue").click()

        # Checar carrinho
        catPage = driver.find_element(By.XPATH, "//*[@class='title']")
        print(catPage.text)
        assert catPage.text == "Checkout: Overview"

        # Finalizar carrinho
        driver.find_element(By.ID, "finish").click()

        # Mensagem final
        checkComplete = driver.find_element(By.XPATH, "//*[@class='complete-header']")
        print(checkComplete.text)
        assert checkComplete.text == "Thank you for your order!"

        # Voltar para home
        driver.find_element(By.ID, "back-to-products").click()
        time.sleep(3)