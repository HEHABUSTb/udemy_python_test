import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Select locale here")
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose chrome or firefox')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        request.cls.browser = browser
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', language)
        profile.update_preferences()
        browser = webdriver.Firefox(firefox_profile=profile)
        request.cls.browser = browser

    yield browser
    print("\nquit browser..")
    browser.quit()
