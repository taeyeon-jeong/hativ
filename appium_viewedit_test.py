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
 
from appium_login_test import TestLogin
 
 
class TestViewEditClick(unittest.TestCase):
 
    driver = None
    wait = None
 
    @classmethod
    def setUpClass(cls):
        cls.driver = TestLogin.driver
        cls.wait = TestLogin.wait
        if cls.driver is None or cls.wait is None:
            raise RuntimeError("TestLogin driver or wait is not initialized")
 
    # 하단 탭에서 메인 화면(홈)으로 전환
    def test_ak_tab1(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(0, 2024)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)
 
    # 메인 화면에서 아래로 스크롤
    def test_al_scroll(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(373, 1046)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(371, 350)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)
 
    # 메인 화면에서 화면 편집 선택
    def test_am_editclick(self):
        el_click = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("화면 편집")',
            )
        )
        el_click.click()
        time.sleep(1)
 
    # 화면 편집 화면에서 혈압 토글 버튼 off로 변경
    def test_an_edittoggle1(self):
        # el_toggle1 = self.wait.until(
        #     lambda x: x.find_element(
        #         AppiumBy.ANDROID_UIAUTOMATOR,
        #         value='new UiSelector().className("android.widget.Switch").instance(0)',
        #         AppiumBy.XPATH, value='//android.widget.Switch[@content-desc="혈압"]'
        #     )
        # )
        # el_toggle1.click()
        # time.sleep(1)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(927, 314)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)
 
    # 화면 편집 화면에서 체온 토글 버튼 off로 변경
    def test_ao_edittoggle2(self):
        # el_toggle1 = self.wait.until(
        #     lambda x: x.find_element(
        #         AppiumBy.ANDROID_UIAUTOMATOR,
        #         value='new UiSelector().className("android.widget.Switch").instance(1)',
        #         AppiumBy.XPATH, value='//android.widget.Switch[@content-desc="체온"]'
        #     )
        # )
        # el_toggle1.click()
        # time.sleep(1)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(927, 485)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)
 
    # 화면 편집 화면에서 뒤로가기 선택하여 메인화면(홈)으로 전환
    def test_ap_backmain(self):
        # el_backmain = self.wait.until(
        #     lambda x: x.find_element(
        #         AppiumBy.ANDROID_UIAUTOMATOR,
        #         value='new UiSelector().className("android.widget.ImageView").instance(0)',
        #     )
        # )
        # el_backmain.click()
        # time.sleep(2)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(70, 150)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)
 
    @classmethod
    def tearDownClass(cls):
        pass  # 여기를 비워두면 테스트 후 driver를 종료하지 않음
 
 
if __name__ == "__main__":
    unittest.main()