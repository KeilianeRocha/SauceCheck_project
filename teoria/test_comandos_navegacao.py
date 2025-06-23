import time
from selenium import webdriver


# Comando de navegação, tem () prq pode chamar um método

browser = webdriver.Chrome()
#pode ser qualquer nome aqui no lugar do 'browser'

# (maximize_window()) → maximiza a tela
browser.maximize_window()

# (get()) → captura a pagina da url
browser.get("https://google.com")
time.sleep(2)

# (refresh()) → atualiza a página
browser.refresh()
time.sleep(2)

# Abre nova aba no navegador
browser.maximize_window()
browser.get("https://one.google.com")

# (back()) → volta para a primeira aba
browser.back()
time.sleep(2)

# (forward()) → volta para a última aba aberta
browser.forward()
time.sleep(2)

# Abre nova guia
browser.switch_to.new_window("tab")
time.sleep(5)

# (close()) → fecha última aba aberta
browser.close()
time.sleep(2)

# (quit()) → fecha todas as abas
browser.quit()
