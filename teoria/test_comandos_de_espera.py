import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Comandos de espera (wait) dentro de 'element.'

# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste
browser.implicitly_wait(12) # fica fazendo verificação ate fazer o teste

# Acessa página
browser.maximize_window()
browser.get("https://leogcarvalho.github.io/test-automation-practice/")

checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")
checkbox.click()
assert checkbox.is_displayed()

show_alert = browser.find_element(By.ID, "alert-button")
show_alert.click()


time.sleep(5)


# time.sleep() → ele sempre vai esperar o tempo que foi setado / não é o mais indicado
"""
time.sleep()
implicit_wait
explicit_wait
"""