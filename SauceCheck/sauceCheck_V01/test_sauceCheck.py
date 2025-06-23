import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Configurar as opções do Chrome para abrir aba anônima
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo

# Inicializar o driver do Chrome com as opções
driver = webdriver.Chrome(options=chrome_options)

# Abrir o site desejado (ex: SauceDemo)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(5)

# Fechar o navegador após o teste (opcional)
# driver.quit()