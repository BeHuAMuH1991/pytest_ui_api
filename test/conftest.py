import allure
import pytest
from selenium import webdriver
from api.BoardApi import BoardApi


@pytest.fixture
def browser():
    with allure.step("Открыть браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> BoardApi:
    return BoardApi("https://api.trello.com/1/", "62979d93ce5f5f881035c524/ATTSE1qlqYpi5GsabKFmJvTWqSkyYHs10So9QwqFGrIFSKXT0r5N32DuqLvz6bnrP2J61825288A")

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi("https://api.trello.com/1/", "")

@pytest.fixture
def create_dummy_board():
    api  = BoardApi("https://api.trello.com/1/", "62979d93ce5f5f881035c524/ATTSE1qlqYpi5GsabKFmJvTWqSkyYHs10So9QwqFGrIFSKXT0r5N32DuqLvz6bnrP2J61825288A")
    resp = api.create_board("Доска для удаления").get("id")
    return resp

@pytest.fixture
def delete_board() ->str:
    dictionary = {"board_id" : ""}
    yield dictionary
    api  = BoardApi("https://api.trello.com/1/", "62979d93ce5f5f881035c524/ATTSE1qlqYpi5GsabKFmJvTWqSkyYHs10So9QwqFGrIFSKXT0r5N32DuqLvz6bnrP2J61825288A")
    resp = api.remove_board(dictionary.get("board_id"))
