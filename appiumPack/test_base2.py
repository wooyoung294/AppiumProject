import time

import pytest
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

@pytest.fixture(scope="module")
def driver():

    # Appium Inspector의 Capability Builder의 값과 동일함
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("appium:automationName", "uiautomator2")
    options.set_capability("locale", "US")
    options.set_capability("language", "en")
    # options.set_capability("app", "path/***.apk")
    # options.set_capability("appPackage", "com.ex.app")

    # UiAutomator2Options 값을 dict형태로 변환
    # myCapabilities = dict(
    #     platformName='Android',
    #     automationName='Uiautomator2',
    #     locale='CN',
    #     language='zh'
    # )

    # Appium 서버 주소
    appium_server_url = 'http://localhost:4723'

    # 서버로 연결해
    driver = webdriver.Remote(appium_server_url, options=options)

    # driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(myCapabilities))

    # 테스트 끝날 때까지 기다려
    yield driver
    # 홈버튼 눌러
    driver.press_keycode(3)
    # 연결 종료해
    driver.quit()

# @pytest.fixture(scope="function")
# def driver(moduleDriver):
#     yield moduleDriver
#     moduleDriver.press_keycode(3)

def getElement(driver, by,value):

    # 찾는 조건이 XPATH 일 경우
    if by == 'XPATH':
        return driver.find_element(by=AppiumBy.XPATH, value=value)
    # 찾는 조건이 ID 일 경우
    elif by == 'ACCESS_ID':
        return driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=value)

    print("language:", driver.capabilities['language'])
    # if driver.capabilities['language'] == 'zh':
    #     return driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="时钟"]')

def test_clickClock(driver):
    # clock = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Clock')
    # clock = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Clock"]')
    # clock = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Clock"]')
    clock = getElement(driver,'XPATH','//android.widget.TextView[@content-desc="Clock"]')
    clock.click()
    time.sleep(1)
    alarmText = getElement(driver,'XPATH', '//android.widget.FrameLayout[@content-desc="Alarm"]')
    assert alarmText.is_displayed()

def test_clickCamera(driver):
    camera = getElement('XPATH', '//android.widget.TextView[@content-desc="Camera"]')
    camera.click()

# 두개의 테스트를 한번에 실행하기 위해 class 생성
class TestClickApps:
    # class 사용시 첫번째 인자로 self 넣어줘야함
    def test_clickClock(self,driver):
        clock = getElement(driver,'XPATH','//android.widget.TextView[@content-desc="Clock"]')
        clock.click()
        time.sleep(1)
        alarmText = getElement(driver,'XPATH', '//android.widget.FrameLayout[@content-desc="Alarm"]')
        assert alarmText.is_displayed()
    def test_clickCamera(self,driver):
        camera = getElement('XPATH', '//android.widget.TextView[@content-desc="Camera"]')
        camera.click()
