from pytest import mark


@mark.xfail(reason="Env was not QA")
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == '80'


def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == '8080'


@mark.skip(reason="Not a staging environment")
def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    assert base_url == 'staging'


# @mark.wip  --  This is custom, not pytest default, not recommended
@mark.skip("Broken, fxing next sprint (do NOT use wip - work in progress)")
def test_this_need_word():
    assert False
