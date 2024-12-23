import time

import pytest
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(scope="module")
def driver():
    # Appium Inspector의 Capability Builder 값과 동일함
    options = UiAutomator2Options()
    # 우영   =  원숭이

    options.set_capability("platformName", "Android")
    options.set_capability("appium:automationName", "uiautomator2")
    options.set_capability("appium:locale", "CN")
    options.set_capability("appium:language", "zh")
    # options.set_capability("app", "path/***.apk")
    # options.set_capability("appPackage", "com.ex.app")

    # Appium 서버 주소
    appium_server_url = 'http://localhost:4723'

    # 서버로 연결해
    driver = webdriver.Remote(appium_server_url, options=options)

    # 테스트 끝날 때까지 기다려
    yield driver
    # 홈버튼 눌러
    driver.press_keycode(3)
    # 연결 종료해
    driver.quit()

def test_click_clock(driver):
    # clock = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Clock"]')
    # clock = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Clock')
    # clock = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Clock"]')
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Clock")
    el1.click()

    # 1초 기다려
    # time.sleep(1)
    alarmText = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.FrameLayout[@content-desc="Alarm"]')
    assert alarmText.is_displayed()
    # alarmText = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="Alarm"]')
    # assert alarmText.is_displayed()
