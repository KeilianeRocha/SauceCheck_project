import time
from tabnanny import check

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Comandos 'assert' → sempre espera um retorno da condição True

# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste
browser.implicitly_wait(12) # fica fazendo verificação ate fazer o teste

# Acessa página
browser.maximize_window()
browser.get("https://leogcarvalho.github.io/test-automation-practice/")
wait = WebDriverWait(browser, 30)

browser.find_element(By.ID, "test-iframe")
time.sleep(2)
