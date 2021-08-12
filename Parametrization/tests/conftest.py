import json
from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

data_path = 'tests/test_data.json'


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)

    return data


@fixture(params=[
    (webdriver.Chrome, ChromeDriverManager),
    (webdriver.Edge, EdgeChromiumDriverManager)
])
def browser(request):
    browser = request.param[0](request.param[1]().install())

    yield browser

    browser.quit()


@fixture(params=load_test_data(data_path))
def tv_brand_data(request):
    data = request.param
    return data
