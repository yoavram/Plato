import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    

class PlatoTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)
        self.site_url = "http://plato.yoavram.com" # "file:///D:/workspace/curveball_project/plato/index.html" # 

    # def test_github_href(self):
    #     driver = self.browser        
    #     driver.get(self.site_url)
    #     self.assertTrue("Plato" in driver.title)
    #     driver.find_element_by_name("github").click()
    #     self.assertTrue("github.com" in driver.page_source)
        
    def test_download(self):
        driver = self.driver
        driver.get(self.site_url)
        btn = driver.find_element_by_class_name('octicon-arrow-down')
        assert btn != None
        btn.click()
        btn_download = self.driver.find_element_by_id('btnDownload')
        assert btn_download != None
        href = btn_download.get_attribute('href')
        
        script = """var x = new XMLHttpRequest();
        x.onload = function() {
            var div = document.createElement('div');
            div.id = 'test';
            div.innerText = x.responseText;
            document.body.appendChild(div)            
        };
        x.open('get', '%s');
        x.send();""" % href        
        driver.execute_script(script)
        test_div = driver.find_element_by_id('test')
        print test_div.text


    def tearDown(self):        
        self.driver.close()


if __name__ == "__main__":
    unittest.main()