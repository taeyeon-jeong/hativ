import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
    NoSuchElementException,
)
import time
 
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
 
capabilities = dict(
    platformName="Android",
    automationName="uiautomator2",
    deviceName="RFCWB12XVPT",
    appPackage="co.vuno.app.hativ.hativ",
    appActivity="co.vuno.app.hativ.hativ.MainActivity",
)
 
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
 
 
class TestLogin(unittest.TestCase):
    driver = None  # driver를 클래스 변수로 선언
    wait = None  # wait 객체 선언
    button_1 = (AppiumBy.ACCESSIBILITY_ID, '설정 완료')
 
    @classmethod
    def setUpClass(cls):
        if cls.driver is None:  # driver가 초기화되지 않았을 경우에만 초기화
            cls.driver = webdriver.Remote(
                "http://127.0.0.1:4723/wd/hub", options=capabilities_options
                # "http://127.0.0.1:4723", options=capabilities_options
            )
 
        cls.wait = WebDriverWait(
            cls.driver,
            10,
            poll_frequency=2,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
                NoSuchElementException,
            ],
        )

    # 알림 허용 팝업에서 허용 선택
    def test_aa_allow(self):
        elaa = self.wait.until(
            lambda x: x.find_element(
                # AppiumBy.XPATH, value='//android.widget.Button[@content-desc="확인"]'
                AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
            )
        )
        elaa.click()
 
    # 최초 나오는 확인 팝업에서 확인 선택
    def test_aa_start(self):
        ele = self.wait.until(
            lambda x: x.find_element(
                # AppiumBy.XPATH, value='//android.widget.Button[@content-desc="확인"]'   ## 아래 코드랑 동일일
                AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().description("확인")'
                # AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
            )
        )
        ele.click()

    # 1차 로그인, change/0913으로 dev서버로 연결 변경
    def test_ab_login(self):
        el_id = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.ImageView").instance(1)',
            )
        )
        el_id.click()
        el_id.send_keys("change")
 
        el_pw = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiSelector().className("android.widget.ImageView").instance(2)',
        )
 
        el_pw.click()
        el_pw.send_keys("0913")
        el_login = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().description("로그인")'
        )
        el_login.click()

    # Api Endpoint 버튼
    def test_ac_next(self):
        elen = self.wait.until(
            lambda x: x.find_element(
                # AppiumBy.XPATH, value='//android.widget.Button[@content-desc="설정 완료"]'
                # AppiumBy.XPATH, value='//android.view.View[@content-desc="Prod"]'
                # AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().description("설정 완료")'
                # AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().description("Prod")'
                
                # AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.widget.Button").index(7)',
                # AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.view.View").index(2)',
                AppiumBy.ACCESSIBILITY_ID, value='설정 완료'
            )
        )
        elen.click()

    # 실제 qa계정으로 dev서버로 로그인 실행
    def test_ad_login(self):
        el_id = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.ImageView").instance(1)',
            )
        )
        el_id.click()
        el_id.clear()
        el_id.send_keys("qa21")
 
        el_pw = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiSelector().className("android.widget.ImageView").instance(2)',
        )
 
        el_pw.click()
        el_pw.clear()
        el_pw.send_keys("qwer1234!")
 
        el_login = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().description("로그인")'
        )
        el_login.click()
 
    # 위치정보 액세스 - 앱 사용 중에만 혀용
    def test_ae_perm(self):
        elen = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
            )
        )
        elen.click()

    # 허용
    def test_af_permAllow(self):
        elen = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
            )
        )
        elen.click()
        ## 5초를 기다리는데 5초안에 웹페이지를 load 하면 바로 넘어가도록
        self.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        pass  # 여기를 비워두면 테스트 후 driver를 종료하지 않음
 
 
if __name__ == "__main__":
    unittest.main()