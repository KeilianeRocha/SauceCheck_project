import time
import pytest
from tests import conftest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginInvalido
class TestCT02:
    def test_ct02_login_invalido(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("test_errorzz")
        driver.find_element(By.ID, "login-button").click()

        alert_erro_messagen = driver.find_element(By.XPATH, "//*[@class='error-message-container error']")
        print(alert_erro_messagen.text)
        assert alert_erro_messagen.text == "Epic sadface: Username and password do not match any user in this service"
        time.sleep(3)