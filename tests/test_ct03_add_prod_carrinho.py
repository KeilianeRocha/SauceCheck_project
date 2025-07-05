import time
import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


# Comandos 'assert' → sempre espera um retorno da condição True
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT03:
    def test_ct03_add_prod_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        # declarando as variaveis
        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"

        # Faz login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Selecionar produto 1
        home_page.adicionar_item_ao_carrinho(produto_1)

        # verificar se produto 1 foi adicionado
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # continuar comprando
        carrinho_page.clicar_continuar_comprando()

        # Selecionar produto 2
        home_page.adicionar_item_ao_carrinho(produto_2)

        # verificar se produto 2 foi adicionado
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_2)
        time.sleep(2)