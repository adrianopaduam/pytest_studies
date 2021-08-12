from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@fixture(scope="session")
def chrome_browser():
    # Setup
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test execution
    yield browser

    # Tear down
    browser.quit()
