import allure
import pytest
from selenium import webdriver
from api.BoardApi import BoardApi
from pa.MainPage import MainPage
from configuration.ConfigProvider import ConfigProvider
from data.DataProvider import DataProvider


@pytest.fixture
def browser():
    with allure.step("Открыть браузер"):

        timeout = ConfigProvider().getint("ui", "timeout")

        browser = webdriver.Chrome()
        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> BoardApi:
    
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url, DataProvider().get("token"))

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi(ConfigProvider().get("api", "base_url"), "")

@pytest.fixture
def create_dummy_board():
    api  = BoardApi(ConfigProvider().get("api", "base_url"), DataProvider().get("token"))
    resp = api.create_board("Доска для удаления").get("id")
    return resp

@pytest.fixture
def delete_board() ->str:
    yield
    ui = MainPage()
    ui.delete_board

@pytest.fixture
def test_data():
    return DataProvider()
