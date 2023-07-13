import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

def generate_options():
    classic_options = {
        "app": "C:\\Users\\salom\\Desktop\\salomon\\levelEditor.exe",
        "platformName": "Windows",
        "automationName": "Windows",
        "deviceName": "DESKTOP-V51L1R3"
    }

    use_existing_app_options = {
        "appTopLevelWindow": None,
        "platformName": "Windows",
        "automationName": "Windows",
    }

    return [classic_options, use_existing_app_options]


@pytest.fixture(params=generate_options())
def driver(request):
    drv = webdriver.Remote('http://127.0.0.1:4723', desired_capabilities=request.param)
    yield drv
    drv.quit()


def test_click_level(driver):
    driver.find_element_by_accessibility_id("Open Level.<empty>.LevelEditor - 1.0.0").click()



