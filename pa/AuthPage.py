import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, __driver: WebDriver):
        self.__url = "https://trello.com/login"
        self.__driver = __driver

    @allure.step("Открыть страницу для авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email} : {password}")
    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.CSS_SELECTOR, "input#user").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "input#login").click()
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "svg[role=presentation]")))
        self.__driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "button#login-submit").click()



