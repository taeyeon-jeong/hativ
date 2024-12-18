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
 
 
class TestBottomTab(unittest.TestCase):
 
    driver = None
    wait = None
 
    @classmethod
    def setUpClass(cls):
        cls.driver = TestLogin.driver
        cls.wait = TestLogin.wait
        if cls.driver is None or cls.wait is None:
            raise RuntimeError("TestLogin driver or wait is not initialized")
 
    # 하단 2번째 탭 건강기록 선택
    def test_ag_tab2(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        # 터치 포인터를 특정 좌표로 이동
        actions.w3c_actions.pointer_action.move_to_location(267, 2040)
        # 현재 좌표(위 코드에서 지정한)에서 동작(화면을 누름)
        actions.w3c_actions.pointer_action.pointer_down()
        # 터치를 0.1초 동안 유지. pause는 시간 단위로 당직을 멈추는 기능(길이 조절)
        actions.w3c_actions.pointer_action.pause(0.1)
        # 터치 동작을 해제(=손가락을 화면에서 뗌)
        actions.w3c_actions.pointer_action.release()
        # 위에서 정의한 모든 터치 동작을 실행행
        actions.perform()
        self.driver.implicitly_wait(5)
        # 마지막 코드 실행 후 2초간 대기 - 생성 후 확인을 위해해
        time.sleep(2)
 
    # 하단 3번째 탭 커뮤니티 선택
    def test_ah_tab3(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(432, 2024)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.driver.implicitly_wait(5)
        time.sleep(4)
 
    # 하단 5번째 탭 마이페이지 선택(하티브몰은 패스)
    def test_ai_tab5(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(864, 2024)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.driver.implicitly_wait(5)
        time.sleep(2)
 
    @classmethod
    def tearDownClass(cls):
        pass  # 여기를 비워두면 테스트 후 driver를 종료하지 않음
 
 
if __name__ == "__main__":
    unittest.main()