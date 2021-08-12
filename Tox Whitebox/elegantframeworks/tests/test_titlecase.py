from titlecase import title_case


class TitleCaseTests:
    def test_lower_text_is_uppercased_properly(self):
        initial = 'this should be capitalized'
        expected = 'This Should Be Capitalized'
        returned_text = title_case(initial)
        assert returned_text == expected
