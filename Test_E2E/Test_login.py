from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_mailEmpty(driver):
    emailField = driver.find_element(By.ID, "user-name")
    emailField.send_keys("")
    passwordField = driver.find_element(By.ID, "password")
    passwordField.send_keys("secret_sauce")
    time.sleep(2)
    loginButton = driver.find_element(By.ID,"login-button")
    loginButton.click()
    time.sleep(2)



def test_passwordEmpty(driver):
    driver.refresh()
    emailField = driver.find_element(By.ID, "user-name")
    emailField.send_keys("standard_user")
    time.sleep(2)
    passwordField = driver.find_element(By.ID,"password")
    passwordField.send_keys("")
    time.sleep(2)
    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()
    time.sleep(2)

def test_loginEmpty(driver):
    driver.refresh()
    emailField = driver.find_element(By.ID, "user-name")
    emailField.send_keys("")
    time.sleep(2)
    passwordField = driver.find_element(By.ID, "password")
    passwordField.send_keys("")
    time.sleep(2)
    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()
    time.sleep(2)

def test_loginSuccess(driver):
    driver.refresh()
    emailField = driver.find_element(By.ID, "user-name")
    emailField.send_keys("standard_user")
    time.sleep(2)
    passwordField = driver.find_element(By.ID, "password")
    passwordField.send_keys("secret_sauce")
    time.sleep(2)
    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()
    time.sleep(2)


def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(4)
    try:
        test_mailEmpty(driver)
        print(f"Teste de email vazio executado com sucesso.")

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    try:
        test_passwordEmpty(driver)
        print(f"Teste de senha vazia executado com sucesso.")

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    try:
        test_loginEmpty(driver)
        print(f"Teste de login vazio executado com sucesso.")

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    try:
        test_loginSuccess(driver)
        print(f"Teste de login bem-sucedido executado com sucessso.")

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    driver.quit()

if __name__ == "__main__":
    test_login()
