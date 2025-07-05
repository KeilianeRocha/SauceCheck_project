from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests import conftest


class HomePage(BasePage):


    def __init__(self): # organizando os locatos
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//*[@class='app_logo']")
        self.item_inventario = (By.XPATH, "//*[@data-test='inventory-item-name' and text()='{}']")
        self. botao_adicionar_carrinho = (By.ID, "add-to-cart")
        self.icone_carinho = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verificar_login_sucesso(self):
        self.verificar_elemento_existe(self.titulo_pagina)

    def adicionar_item_ao_carrinho(self, nome_item):# agora esse nome capturado passa a ser dinamico
        item_locator = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item_locator)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carinho)



