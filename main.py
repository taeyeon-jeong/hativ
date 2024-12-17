import unittest
from appium_login_test import TestLogin
from appium_bottomtab_test import TestBottomTab
from appium_viewedit_test import TestViewEditClick
from appium_pressure_test import TestBloodPressure
 
# 테스트 스위트 생성
def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestLogin))
    suite.addTests(loader.loadTestsFromTestCase(TestBottomTab))
    suite.addTests(loader.loadTestsFromTestCase(TestViewEditClick))
    suite.addTests(loader.loadTestsFromTestCase(TestBloodPressure))
 
    return suite
 
 
if __name__ == "__main__":
    # 테스트 실행
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())