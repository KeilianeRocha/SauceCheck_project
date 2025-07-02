from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests import conftest



class LoginPage(BasePage):


    def __init__(self): # organizando os locatos
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button= (By.ID, "login-button")

    def fazer_login(self, user, password):
        """self.driver.find_element(*self.username_field).send_keys(user)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()"""

# melhoria do cód de cima
        self.enviar_credenciais(self.username_field, user)
        self.enviar_credenciais(self.password_field,password)
        self.clicar(self.login_button)
