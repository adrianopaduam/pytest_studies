from pytest import mark


@mark.ui
@mark.body
class BodyTests:

    @mark.door
    def test_body_functions_as_expected(self):
        assert True

    def test_body_functions_as_expected_no_door(self, chrome_browser):
        chrome_browser.get("https://www.eldorado.org.br")
        assert True
