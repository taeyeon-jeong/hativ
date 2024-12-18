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
from appium_pressure_test import TestBloodPressure
 
 
class TestBloodSugar(unittest.TestCase):
 
    driver = None
    wait = None
 
    @classmethod
    def setUpClass(cls):
        cls.driver = TestLogin.driver
        cls.wait = TestLogin.wait
        if cls.driver is None or cls.wait is None:
            raise RuntimeError("TestLogin driver or wait is not initialized")
 
    # pressure에서 하단 건강기록 탭 유지 상태라고 가정. 혈당 탭 선택
    def test_be_bsugartab(self):
        self.driver.implicitly_wait(5)
        el_bsugar = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.view.View").index(4)',
                value='new UiSelector().description("혈당\n탭 5개 중 4번째")',
            )
        )
        el_bsugar.click()
        self.driver.implicitly_wait(5)
 
    # 혈당 추가 버튼 선택
    def test_bf_bsugaradd(self):
        self.driver.implicitly_wait(5)
        el_sugaradd = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("입력")',
            )
        )
        el_sugaradd.click()
        self.driver.implicitly_wait(5)
 
    # 측정 시간 선택에서 식사 후 선택
    def test_bg_selecttime(self):
        el_selecttime = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.view.View").index(4)',
                value='new UiSelector().description("식사 후")',
            )
        )
        el_selecttime.click()
        self.driver.implicitly_wait(5)

    def test_bga_selecttime(self):
        el_selecttime = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("다음")',
            )
        )
        el_selecttime.click()
        self.driver.implicitly_wait(5)

    # 혈당 추가에서 120입력하고 메모 입력
    def test_bh_inputsugar(self):
        el_inputsugar = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(0)',
            )
        )
        el_inputsugar.click()
        el_inputsugar.send_keys("120")
        self.driver.implicitly_wait(5)
 
    def test_bi_sugarmemo(self):
        el_sugarmemo = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(1)',
            )
        )
        el_sugarmemo.click()
        el_sugarmemo.send_keys("식사 후 5분후에 작성함")
        self.driver.implicitly_wait(5)
 
    # 혈당 추가에서 저장 버튼 선택
    def test_bj_save(self):
        el_save = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("저장")',
            )
        )
        el_save.click()
        self.driver.implicitly_wait(5)
 
    # 혈당 화면에서 카드 선택
    def test_bk_selectcard(self):
        el_selectcard = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.widget.ImageView").index(0)',
                value='new UiSelector().className("android.widget.ImageView").instance(1)',
            )
        )
        el_selectcard.click()
        self.driver.implicitly_wait(5)
        time.sleep(2)
 
    # 혈당 기준표 선택
    def test_bl_sugartable(self):
        el_sugartable = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("혈당 기준표")',
            )
        )
        el_sugartable.click()
        self.driver.implicitly_wait(5)
        time.sleep(2)
        self.driver.back()
 
    # 카드 더보기 버튼 재사용(호출)
    def test_bm_deletemenu(self):
        # TestBloodPressure의 test_bba_deletemenu 메서드를 호출
        deletemenu_button = TestBloodPressure()
        deletemenu_button.driver = self.driver  # 공유된 driver 사용
        deletemenu_button.wait = self.wait  # 공유된 wait 사용
        deletemenu_button.test_bc_deletemenu()  # 호출
        deletemenu_button.test_bcb_deletemenu() # 수정 버튼 클릭 호출

    # 수정 - 130입력
    def test_bn_inputsugar(self):
        el_inputsugar = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(0)',
            )
        )
        el_inputsugar.click()
        el_inputsugar.send_keys("130")
        self.driver.implicitly_wait(5)

    # 수정 - 측정 시기 선택
    def test_bo_timeModify(self):
        el_timeModify = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.view.View").instance(1)',
                value='new UiSelector().description("식사 후")',
            )
        )
        el_timeModify.click()
        self.driver.implicitly_wait(5)

    # 측정 시기 스크롤
    def test_boa_scroll(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(400, 1740)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(400, 2200)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.driver.implicitly_wait(5)

    # 측정 시기 아침 공복 선택
    def test_bob_timeModify2(self):
        el_sugartable = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("아침 공복")',
            )
        )
        el_sugartable.click()
        self.driver.implicitly_wait(5)
        self.test_bj_save() # 저장버튼 클릭 호출
        
 
    # 수정 - 메모 수정 후 저장
    def test_bp_sugarmemo(self):
        el_sugarmemo = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(1)',
            )
        )
        el_sugarmemo.click()
        el_sugarmemo.send_keys("식사 후 5분후 -> 아침 공복 10분후 수정")
        self.driver.implicitly_wait(5)
        self.test_bj_save() # 저장버튼 클릭 호출
        self.test_bk_selectcard() # 카드 선택 호출
        
    # 추가 메뉴에서 삭제 선택
    def test_bq_deletesugar(self):
        # TestBloodPressure의 test_bbb_selectdelete 메서드를 호출
        selectdelete_button = TestBloodPressure()
        selectdelete_button.driver = self.driver  # 공유된 driver 사용
        selectdelete_button.wait = self.wait  # 공유된 wait 사용
        selectdelete_button.test_bc_deletemenu() # 더보기 메뉴 클릭 호출
        selectdelete_button.test_bd_selectdelete()  # 삭제 버튼 클릭 호출
        selectdelete_button.test_bda_deleteconfirm()  # 확인 팝업 삭제 확인 호출출
 
    # 삭제 확인 팝업에서 삭제 버튼 선택하여 삭제 실행
    # def test_br_deleteconfirm(self):
    #     # TestBloodPressure의 test_bbc_deleteconfirm 메서드를 호출
    #     deleteconfirm_button = TestBloodPressure()
    #     deleteconfirm_button.driver = self.driver  # 공유된 driver 사용
    #     deleteconfirm_button.wait = self.wait  # 공유된 wait 사용
    #     deleteconfirm_button.test_bda_deleteconfirm()  # 호출
 
    # 혈당 통계 화면 진입
    def test_br_stats(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(992, 163)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.driver.implicitly_wait(5)
 
    # 혈당 통계에서 주>월>년>최근 순으로 탭 확인
    def test_bra_weeks(self):
        el_sugarweeks = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                value="주",
            )
        )
        el_sugarweeks.click()
        self.driver.implicitly_wait(5)

        el_sugarmonth = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                value="월",
            )
        )
        el_sugarmonth.click()
        self.driver.implicitly_wait(5)

        el_sugaryears = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                value="년",
            )
        )
        el_sugaryears.click()
        self.driver.implicitly_wait(5)

    # 아침 공복 체크박스
        el_sugarCheckBox = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.XPATH, value='//android.widget.Button[@content-desc="아침 공복"]/android.widget.CheckBox'
            )
        )
        el_sugarCheckBox.click()
        self.driver.implicitly_wait(5)

        el_sugarrecent = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                value="최근",
            )
        )
        el_sugarrecent.click()
        self.driver.implicitly_wait(5)
 
    # 혈당 통계에서 엑셀 버튼 선택해서 월별선택/기간선택 화면에서 기간 선택
    def test_bu_period(self):
        el_sugarstats = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.XPATH,
                value='//android.view.View[@content-desc="혈당 통계"]/android.widget.ImageView[2]',
            )
        )
        el_sugarstats.click()
        self.driver.implicitly_wait(5)

        el_sugarperiod = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("기간선택")',
            )
        )
        el_sugarperiod.click()
        self.driver.implicitly_wait(5)

        el_sugarback = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.XPATH,
                value='//android.view.View[@content-desc="혈당"]/android.widget.ImageView[1]',
            )
        )
        el_sugarback.click()
        self.driver.implicitly_wait(5)
        
        el_sugarback2 = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.XPATH,
                value='//android.view.View[@content-desc="혈당 통계"]/android.widget.ImageView[1]',
            )
        )
        el_sugarback2.click()
        self.driver.implicitly_wait(5)
 
    @classmethod
    def tearDownClass(cls):
        pass  # 여기를 비워두면 테스트 후 driver를 종료하지 않음
 
 
if __name__ == "__main__":
    unittest.main()