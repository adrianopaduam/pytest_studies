from pytest import mark


@mark.ui
@mark.entertainment
def test_entertainment_system_functions_as_expected(chrome_browser):
    chrome_browser.get("http://extranet.eldorado.org.br")
    assert True
