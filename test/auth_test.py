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
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "behuamuh078")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    assert info[0] == "Алeксей Торхов"
    assert info[1] == email
    assert main_page.get_current_url().endswith("torhovaleksej/boards") 
