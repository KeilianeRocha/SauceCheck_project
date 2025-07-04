import time
import pytest
from driver import driver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests import conftest
from selenium.webdriver.common.by import By


# Comandos 'assert' → sempre espera um retorno da condição True
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT03:
    def test_ct03_add_prod_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()

        # Faz login
        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_sucesso()

        #homepage = driver.find_element(By.XPATH, "//*[@class='app_logo']")
        #print(homepage.text)
        #assert homepage.text == "Swag Labs"

        # Selecionar produto 1
        driver.find_element(By.ID, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Selecionar produto 2
        driver.find_element(By.ID, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # visualizar no carro
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        checkproduct = driver.find_element(By. XPATH, "//*[@class='inventory_item_name']")
        print(checkproduct.text)
        assert checkproduct.text == "Sauce Labs Backpack"
        time.sleep(3)
