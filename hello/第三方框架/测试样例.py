import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://www.python.org')
        self.assertIn("Python",driver.title)
        elem = driver.find_element_by_name('q')
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results founds." not in driver.page_source

    def tearDown(self):
        # 关闭这个页面
        self.driver.close()
        # 退出整个浏览器
        # self.driver.quit()

# 用来区分模块，多个模块中都含有main入口时，用这个区别开来
if __name__ == '__main__':
    unittest.main()