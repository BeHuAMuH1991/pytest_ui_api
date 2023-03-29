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


    @allure.step("Создать новую доску")
    def create_board(self, name):
        self.__driver.find_element(By.CSS_SELECTOR, ".board-tile.mod-add").click()
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='create-board-title-input']").send_keys(name)
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='create-board-submit-button']").click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        name_board = self.__driver.find_element(By.CSS_SELECTOR, "h1")
        
        return name_board.text
    
    def delete_board(self):
        self.__driver.find_element(By.CSS_SELECTOR, ".frrHNIWnTojsww.GDunJzzgFqQY_3.bxgKMAm3lq5BpA.HAVwIqCeMHpVKh.SEj5vUdI3VvxDc").click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".board-menu-navigation-item-link.js-open-more")))
        self.__driver.find_element(By.CSS_SELECTOR, ".board-menu-navigation-item-link.js-open-more").click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".board-menu-navigation-item-link.js-close-board")))
        self.__driver.find_element(By.CSS_SELECTOR, ".board-menu-navigation-item-link.js-close-board").click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".js-confirm.full.nch-button.nch-button--danger")))
        self.__driver.find_element(By.CSS_SELECTOR, ".js-confirm.full.nch-button.nch-button--danger").click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='close-board-delete-board-button']")))
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='close-board-delete-board-button']").click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='close-board-delete-board-confirm-button']")))
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='close-board-delete-board-confirm-button']").click()

