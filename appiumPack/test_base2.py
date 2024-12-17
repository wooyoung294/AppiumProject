import pytest
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver.remote.webelement import WebElement

def getElement(driver, by,value):
    print('getElement',driver.capabilities['platformName'])
    if by == 'XPATH':
        return driver.find_element(by=AppiumBy.XPATH, value=value)
    elif by == 'ACCESS_ID':
        return driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=value)
@pytest.fixture(scope="module")
def driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "uiautomator2")
    options.set_capability("locale", "US")
    options.set_capability("language", "en")
    options.set_capability("app", "path/***.apk")
    options.set_capability("appPackage", "com.ex.app")

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=options)

    yield driver
    driver.quit()

# @pytest.fixture(scope="module")
# def driver():
#     capabilities = dict(
#         platformName='Android',
#         automationName='Uiautomator2',
#     )
#
#     appium_server_url = 'http://localhost:4723'
#
#     driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
#
#
#     yield driver
#     driver.quit()

def test_clickClock(driver):
    # clock = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Clock')
    # clock = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Clock"]')
    # clock = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Clock"]')

    clock = getElement(driver,'XPATH','//android.widget.TextView[@content-desc="Clock"]')
    clock.click()

def test_clickWebtoon(driver):
    webtoon = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Naver Webtoon"]')
    webtoon.click()

# class TestClickApps:
#     def test_clickClock(self,driver):
#         clock = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Clock"]')
#         clock.click()
#         assert clock.is_displayed()
#     def test_clickWebtoon(self,driver):
#         webtoon = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Naver Webtoon"]')
#         webtoon.click()