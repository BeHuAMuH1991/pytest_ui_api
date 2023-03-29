import allure
from pa.AuthPage import AuthPage
from pa.MainPage import MainPage


# def test_create_board(browser, test_data):
#     email = test_data.get("email")
#     password = test_data.get("password")
#     name_board = test_data.get("name_board")

#     auth_page = AuthPage(browser)
#     auth_page.go()
#     auth_page.login_as(email, password)

#     main_page = MainPage(browser)
#     board_name = main_page.create_board(name_board)
#     main_page.delete_board()

#     with allure.step("Проверяем название доски"):
#         assert board_name == name_board


def test_delete_board(browser, test_data):
    email = test_data.get("email")
    password = test_data.get("password")
    name_board = test_data.get("name_board")


    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.create_board(name_board)
    main_page.delete_board()






