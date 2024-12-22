from datetime import time
from distutils.util import strtobool

import pytest
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver


def waitElement(driver, xpath):
    try:
        element: WebElement = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    except TimeoutException:
        return False


@pytest.fixture(scope="function")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='Uiautomator2',
        app="/Users/woo02/AndroidStudioProjects/AppiumTestApp/app/build/outputs/apk/debug/app-debug.apk",

    )

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    yield driver
    driver.quit()


class TestLogin:
    def test_SuccessLogin(self,driver):
        name = 'ONYU'
        nameInput = waitElement(driver,
                                 '//android.widget.EditText[@resource-id="com.example.appiumtestapp:id/editTextText"]')
        nameInput.click()
        nameInput.send_keys(name)
        assert nameInput.text == name

        # 이름 입력으로 인해 키보드 올라와서 뒤로가기 버튼으로 내려주기
        driver.execute_script('mobile: pressKey', {"keycode": 4})


        checkBox = waitElement(driver, '//android.widget.CheckBox[@resource-id="com.example.appiumtestapp:id/checkBox"]')
        checkBox.click()
        assert strtobool(checkBox.get_attribute('checked')) == True

        loginBtn = waitElement(driver, '//android.widget.Button[@resource-id="com.example.appiumtestapp:id/button"]')
        loginBtn.click()

        welcomeText = waitElement(driver,
                                   '//android.widget.TextView[@resource-id="com.example.appiumtestapp:id/welcomeText"]')
        assert welcomeText.text == name + '님 환영합니다!!!'

