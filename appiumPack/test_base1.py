import time

import pytest
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


@pytest.fixture(scope="module")
def driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "uiautomator2")

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=options)

    yield driver
    driver.press_keycode(3)
    driver.quit()

def test_clickClock(driver):
    # clock = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Clock')
    clock = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Clock"]')
    # clock = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Clock"]')
    clock.click()
    assert clock.is_displayed()
