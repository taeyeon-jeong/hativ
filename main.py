import unittest
from appium_login_test import TestLogin
 
# 테스트 스위트 생성
def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestLogin))
 
    return suite
 
 
if __name__ == "__main__":
    # 테스트 실행
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())