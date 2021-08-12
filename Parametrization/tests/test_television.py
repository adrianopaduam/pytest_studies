from pytest import mark


# Inline Parametrization
@mark.skip
@mark.parametrize('tv_brand', [('Samsung'), ('Sony'), ('Vizio')])
def test_television_turns_on(tv_brand):
    print(f'{tv_brand} turns on as expected')


# Fixture parametrization
@mark.skip
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://techstepacademy.com/training-ground')


# Fixture with data driven information
def test_television_turns_on_data_from_fixture(tv_brand_data):
    print(f'{tv_brand_data} turns on as expected')
