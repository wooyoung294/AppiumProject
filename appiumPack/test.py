import base64
import os

import allure
import pytest
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver

def wait_Element(driver, xpath):
    location = xpath

    try:
        element:WebElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    except TimeoutException:
        print("Timeout!!!!!!!!!!!!")
        return False


@pytest.fixture(scope="module")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='Uiautomator2',
        app= "/Users/woo02/AndroidStudioProjects/AppiumTestApp/app/build/outputs/apk/debug/app-debug.apk",

    )

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))


    yield driver
    driver.quit()

#3 테스트케이스
@allure.feature('Case1')
@allure.story('Login and Intent View')
def test_case_01(driver):

    SCREENPATH = '/Applications/recording'
    videoFilePath = os.path.join(SCREENPATH, 'recording.mp4')
    driver.start_recording_screen()

    name='ONYU'

    nameInput = wait_Element(driver,
                      '//android.widget.EditText[@resource-id="com.example.appiumtestapp:id/editTextText"]')
    nameInput.click()
    nameInput.send_keys(name)
    assert nameInput.text == name

    allure.attach(driver.get_screenshot_as_png(), name='Login Screen',attachment_type=allure.attachment_type.PNG)

    checkBox = wait_Element(driver,'//android.widget.CheckBox[@resource-id="com.example.appiumtestapp:id/checkBox"]')
    checkBox.click()

    loginBtn = wait_Element(driver,'//android.widget.Button[@resource-id="com.example.appiumtestapp:id/button"]')
    loginBtn.click()

    welcomeText = wait_Element(driver,'//android.widget.TextView[@resource-id="com.example.appiumtestapp:id/welcomeText"]')
    assert welcomeText.text == name + '님 환영합니다!!!'

    videoBase = driver.stop_recording_screen()

    with open(videoFilePath, 'wb') as videoFile:
        videoFile.write(base64.b64decode(videoBase))

    allure.attach(base64.b64decode(videoBase),name="Login Video",attachment_type=allure.attachment_type.MP4)
    allure.attach(driver.get_screenshot_as_png(), name='Main Screen',attachment_type=allure.attachment_type.PNG)


