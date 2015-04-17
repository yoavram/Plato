import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PlatoTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)


    def test_github_href(self):
        browser = self.browser
        #browser.get("http://plato.yoavram.com")
        browser.get("file:///D:/workspace/curveball_project/plato/index.html")
        self.assertTrue("Plato" in browser.title)
        browser.find_element_by_name("github").click()
        self.assertTrue("github.com" in browser.page_source)
        

    def tearDown(self):        
        self.browser.close()


if __name__ == "__main__":
    unittest.main()