import time
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginInvalido
class TestCT02:
    def test_ct02_login_invalido(self):
        texto_esperado = f"Epic sadface: Username and password do not match any user in this service"
        login_page = LoginPage()

        # Verifica se o login foi realizado
        login_page.fazer_login("standard_user", "test_errorzz")

        # verifica se login falhou
        login_page.verificar_se_erro_login_existe()

        # verifica o texto da mensagem de erro
        login_page.verificar_texto_erro_login(texto_esperado)
