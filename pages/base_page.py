from tests import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:


    def __init__(self): # organizando os locatos
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def enviar_credenciais(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela."

    def capturar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text

    def esperar_elemento_aparecer(self, locator, timeout=10): # o timeout é opcional
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # função para verificar se um item esta na tela
    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator), (f"O elemento '{locator}' não foi encontrado!"
                                                                 f"O esperado era que existisse.")
    def verificar_elemento_n_existe(self, locator):
        assert len(self.encontrar_elementos(locator)) == 0, (f"O elemento '{locator}' foi encontrado."
                                                                 f"O esperado era que não existisse.")

    """
     função para dar click duplo em um elemento
    def click_duplo(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()

    # função para dar click com botão direito em um elemento
    def click_botao_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()

    # função usar teclado
    def presionar_tecla(self, locator, key):
        elem = self.encontrar_elemento(locator)
        if key == "ENTER":
            elem.send_keys(Keys.ENTER)
        elif key == "SPACE":
            elem.send_keys(Keys.SPACE)
    # adicionando conforme a necessidade do teste

"""

