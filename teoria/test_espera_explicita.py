import time
from tabnanny import check

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Comandos de espera (wait) dentro de 'element.'

# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste
browser.implicitly_wait(12) # fica fazendo verificação ate fazer o teste

# Acessa página
browser.maximize_window()
browser.get("https://leogcarvalho.github.io/test-automation-practice/")
wait = WebDriverWait(browser, 30)

# Verifica se o alerta esta presente
#browser.find_element(By.ID, "alert-button").click()
#wait.until(EC.alert_is_present())

# verifica se o texto esta presente
browser.find_element(By.ID, "delayed-button").click()
wait.until(EC.text_to_be_present_in_element((By.ID, "delayed-button"), "Show Delayed Message"))
target_text = browser.find_element(By.ID, "delayed-message").text
time.sleep(5)

# verifica se o botão é clicável
browser.find_element(By.ID, "color-button").click()
wait.until(EC.element_to_be_clickable((By.ID, "color-button")))

# esperar o checkbox ser selecionado
checkbox = browser.find_element(By. XPATH, "//*[@value='feature1']")
browser.find_element(By. XPATH, "//*[@value='feature1']").click()
wait.until(EC.element_to_be_selected(checkbox))

time.sleep(3)
#assert alert_button.is_selected()




