import allure
from pa.AuthPage import AuthPage
from pa.MainPage import MainPage
from time import sleep


def test_auth(browser, test_data):
    email = test_data.get("email")
    password = test_data.get("password")
    name = test_data.get("name")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()
    sleep(20)

    with allure.step("Проверяем имя и почту"):
        with allure.step("Имя: "+name):
            assert info[0] == name
        with allure.step("Почта: "+email):
            assert info[1] == email
    with allure.step("Проверяем правильность окончания URL"):
        assert main_page.get_current_url().endswith("torhovaleksej/boards") 
