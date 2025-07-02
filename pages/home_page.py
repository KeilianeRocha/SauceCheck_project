from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import conftest


class HomePage(BasePage):


    def __init__(self): # organizando os locatos
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//*[@class='app_logo']")

    def verificar_login_sucesso(self):
        self.verificar_elemento_existe(self.titulo_pagina)



