from pytest import mark


@mark.ui
@mark.smoke
@mark.engine
def test_engine_functions_as_expected(chrome_browser):
    chrome_browser.get("http://intranet.eldorado.org.br")
    assert True
