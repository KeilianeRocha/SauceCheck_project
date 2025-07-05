from tests import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CarrinhoPage(BasePage):


    def __init__(self): # organizando os locatos
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//*[@data-test='inventory-item-name' and text()='{}']")
        self.botao_continuar_comprando = (By.ID, "continue-shopping")

    def verificar_produto_carrinho_existe(self, nome_item):
        item_locator = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_elemento_existe(item_locator)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando) # metodo para clicar
