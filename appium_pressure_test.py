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
from appium_bottomtab_test import TestBottomTab
 
 
class TestBloodPressure(unittest.TestCase):
 
    driver = None
    wait = None
 
    @classmethod
    def setUpClass(cls):
        cls.driver = TestLogin.driver
        cls.wait = TestLogin.wait
        if cls.driver is None or cls.wait is None:
            raise RuntimeError("TestLogin driver or wait is not initialized")
 
    def test_ao_calltab2(self):
        # TestBottomTab의 test_ah_tab2 메서드를 호출
        # 하단 탭 중 2번째 건강기록 선택
        bottom_tab = TestBottomTab()
        bottom_tab.driver = self.driver  # 공유된 driver 사용
        bottom_tab.wait = self.wait  # 공유된 wait 사용
        bottom_tab.test_ag_tab2()  # 호출
 
    # 건강기록에서 상단 혈압 탭 선택
    def test_ap_pressuretab(self):
        time.sleep(1)
        el_pressure = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.view.View").index(1)',  index 1 이 중복이 존재함..
                value='new UiSelector().description("혈압\n탭 5개 중 2번째")',
            )
        )
        el_pressure.click()
        time.sleep(1)
 
    # 혈압에서 혈압 추가(입력) 버튼 클릭
    def test_aq_pressureaddb(self):
        time.sleep(1)
        el_add = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("입력")',
            )
        )
        el_add.click()
        time.sleep(1)
 
    # 혈압 추가에서 최고 입력 부분 선택 후 120 입력
    def test_ar_max(self):
        el_max = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(0)',
            )
        )
        el_max.click()
        el_max.send_keys("120")
        time.sleep(1)
 
    # 혈압 추가에서 최저 입력 부분 선택 후 80 입력
    def test_as_min(self):
        el_min = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(1)',
            )
        )
        el_min.click()
        el_min.send_keys("80")
        time.sleep(1)
 
    # 혈압 추가에서 맥박 입력 부분 선택 후 85 입력
    def test_at_pulse(self):
        el_pulse = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(2)',
            )
        )
        el_pulse.click()
        el_pulse.send_keys("85")
        time.sleep(1)
 
    # 혈압 추가에서 메모 입력
    def test_au_memo(self):
        el_memo = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(3)',
            )
        )
        el_memo.click()
        el_memo.send_keys("120에 80 그리고 맥박 85 오늘 측정 완료")
        time.sleep(1)
 
    # 혈압 추가에서 저장 버튼 선택
    def test_av_save(self):
        el_save = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("저장")',
            )
        )
        el_save.click()
        time.sleep(3)
 
    # # 혈압 카드 목록에서 첫번째 카드 선택
    def test_aw_pcard(self):
        el_pcard = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.ImageView").instance(3)',
            )
        )
        el_pcard.click()
        time.sleep(2)
 
    # # 혈압 카드 화면에서 평균 설명 부분 선택
    def test_ax_avg(self):
        el_avg = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.view.View").index(1)',
                value='new UiSelector().className("android.widget.Button").instance(0)',
            )
        )
        el_avg.click()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
 
    # # 혈압 카드 화면에서 맥압 설명 부분 선택
    def test_ay_pulsep(self):
        el_pulsep = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.view.View").index(2)',
                value='new UiSelector().className("android.widget.Button").instance(1)',
            )
        )
        el_pulsep.click()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
 
    # # 혈압 카드 화면에서 심부담도 설명 부분 선택
    def test_az_cardiacl(self):
        el_cardiacl = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.view.View").index(3)',
                value='new UiSelector().className("android.widget.Button").instance(2)',
            )
        )
        el_cardiacl.click()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
 
    # # 혈압 카드 화면에서 고혈압 기준표 설명 부분 선택
    def test_ba_hypertension(self):
        el_hypertension = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("고혈압 기준표")',
            )
        )
        el_hypertension.click()
        time.sleep(2)
 
    # # 혈압 카드 화면에서 고혈압 기준표 설명 닫기
    def test_bb_confirm(self):
        el_confirm = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("확인")',
            )
        )
        el_confirm.click()
        time.sleep(1)
 
    # # 추가 메뉴 선택
    def test_bc_deletemenu(self):
        el_deletepressure = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.ImageView").instance(0)',
            )
        )
        el_deletepressure.click()
        time.sleep(2)

    def test_bcb_deletemenu(self):
        el_deletepressure = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("수정")',
            )
        )
        el_deletepressure.click()
        time.sleep(2)
    
     # 수정 - 최고 입력 부분 선택 후 130 입력
    def test_bcc_max(self):
        el_max = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(0)',
            )
        )
        el_max.click()
        el_max.send_keys("130")
        time.sleep(1)
 
    # 수정 - 최저 입력 부분 선택 후 90 입력
    def test_bcd_min(self):
        el_min = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(1)',
            )
        )
        el_min.click()
        el_min.send_keys("90")
        time.sleep(1)
 
    # 수정 - 맥박 입력 부분 선택 후 95 입력
    def test_bce_pulse(self):
        el_pulse = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(2)',
            )
        )
        el_pulse.click()
        el_pulse.send_keys("95")
        time.sleep(1)
 
    # 수정 - 메모 입력
    def test_bcf_memo(self):
        el_memo = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.EditText").instance(3)',
            )
        )
        el_memo.click()
        el_memo.send_keys("130에 90 그리고 맥박 95 오늘 측정 수정")
        time.sleep(1)

    # 수정 - 저장 버튼 선택
    def test_bcg_save(self):
        el_save = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("저장")',
            )
        )
        el_save.click()
        time.sleep(2)
    # 카드 터치 및 더보기 메뉴 한번 더 호출
        self.test_aw_pcard()
        self.test_bc_deletemenu()
        
    # 삭제
    def test_bd_selectdelete(self):
        el_selectdelete = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().description("삭제")',
            )
        )
        el_selectdelete.click()
        time.sleep(1)
 
    # 삭제 확인인
    def test_bda_deleteconfirm(self):
        el_deleteconfirm = self.wait.until(
            lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                # value='new UiSelector().className("android.widget.Button").index(4)',
                value='new UiSelector().className("android.widget.Button").instance(1)',
            )
        )
        el_deleteconfirm.click()
        time.sleep(1)
 
    @classmethod
    def tearDownClass(cls):
        pass  # 여기를 비워두면 테스트 후 driver를 종료하지 않음
 
if __name__ == "__main__":
    unittest.main()