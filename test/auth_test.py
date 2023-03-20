import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pa.AuthPage import AuthPage
from pa.MainPage import MainPage
from time import sleep




def test_auth(browser):
    email = "torhovaleksej@gmail.com"
    password = "behuamuh078"
    name = "Алeксей Торхов"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    with allure.step("Проверяем имя и почту"):
        with allure.step("Имя: "+name):
            assert info[0] == name
        with allure.step("Почта: "+email):
            assert info[1] == email
    with allure.step("Проверяем правильность окончания URL"):
        assert main_page.get_current_url().endswith("torhovaleksej/boards") 
