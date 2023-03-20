import allure 
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, __driver: WebDriver):
        self.__driver = __driver

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url
    
    @allure.step("Открыть меню профиля")
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid=header-member-menu-button]").click()

    @allure.step("Получить данные: Имя и Почту")
    def get_account_info(self) -> list[str]:
        container = self.__driver.find_element(By.CSS_SELECTOR, "[data-testid=account-menu]>div>div:last-child")
        fields = container.find_elements(By.CSS_SELECTOR, "div")

        name = fields[0].text
        email = fields[1].text

        return [name, email]
