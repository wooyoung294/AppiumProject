import pytest
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver

@pytest.fixture(scope="module")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='Uiautomator2',
    )

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))


    yield driver
    driver.quit()

def clickClock(driver):
    clock = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Clock')
    # clock = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Clock"]')
    clock.click()
