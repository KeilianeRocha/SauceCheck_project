from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import conftest


class HomePage(BasePage):


    def __init__(self): # organizando os locatos
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//*[@class='app_logo']")
        self.item_inventario_primeiro = (By.ID, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']")
        self.carrinho_one = (By.ID, "add-to-cart").click()
        self.item_inventario_segundo = (By.ID, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']")
        self.carrinho_two =(By.ID, "add-to-cart").click()



    def verificar_login_sucesso(self):
        self.verificar_elemento_existe(self.titulo_pagina)



