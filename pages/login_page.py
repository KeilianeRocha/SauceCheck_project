from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests import conftest


class LoginPage(BasePage):


    def __init__(self): # organizando os locatos
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.erro_message_login = (By.XPATH, "//*[@class='error-message-container error']")

    def verificar_se_erro_login_existe(self):
        self.verificar_elemento_existe(self.erro_message_login)

    def fazer_login(self, user, password):
        self.enviar_credenciais(self.username_field, user)
        self.enviar_credenciais(self.password_field,password)
        self.clicar(self.login_button)

    def verificar_texto_erro_login(self, texto_esperado):
        texto_encontrado = self.capturar_texto_elemento(self.erro_message_login)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi'{texto_encontrado}' mas era esperado o texto '{texto_esperado}'."

