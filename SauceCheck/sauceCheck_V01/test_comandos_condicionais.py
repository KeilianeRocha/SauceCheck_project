import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Comandos condicionais dentro de 'element.' retornam 'True' ou 'False'

# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste

# Acessa página
browser.maximize_window()
browser.get("https://demo.applitools.com/")

# (find_element()) → encontra uma ocorrência somente / se não encontrar ele retorna ERRO
username = browser.find_element(By.ID, "username")
password = browser.find_element(By.ID, "password")

# (send_keys()) → envia informações para os campos dos elementos anteriores
username.send_keys("teste_teste")
password.send_keys("teste_01")
checkbox_remember_me = browser.find_element(By. XPATH, "//*[@type='checkbox']")

#is_displayed() → printa se o elemento esta na tela
print(username.is_displayed())
# assert username.is_displayed() → esse é uma melhoria no cod.
print(password.is_displayed())
print(checkbox_remember_me.is_displayed())

#is_enabled() → verifica se os campos estão habilitados
print(username.is_enabled())
# assert username.is_enabled() → esse é uma melhoria no cod.
print(password.is_enabled())
print(checkbox_remember_me.is_enabled())

#is_selected() → checkbox antes de clicar
print(checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()

checkbox_remember_me.click()

#is_selected() → checkbox depois de clicar
print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()

time.sleep(2)
