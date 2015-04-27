import unittest
import os
import sys
import new

from selenium import webdriver
from sauceclient import SauceClient

USERNAME = os.environ.get('SAUCE_USERNAME')
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
assert USERNAME, "No SauceLabs USERNAME"
assert ACCESS_KEY, "No SauceLabs ACCESS_KEY"

sauce = SauceClient(USERNAME, ACCESS_KEY)

browsers = [{"platform": "Mac OS X 10.9",
             "browserName": "chrome",
             "version": "31"},
            {"platform": "Windows 8.1",
             "browserName": "internet explorer",
             "version": "11"}]


def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator


@on_platforms(browsers)
class PlatoTestCase(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (USERNAME, ACCESS_KEY)
        )
        self.driver.implicitly_wait(30)
        #self.driver = webdriver.Chrome()
        self.site_url =  "http://plato.yoavram.com" # "file:///D:/workspace/curveball_project/plato/index.html" #        


    def test_github_link(self):
        driver = self.driver        
        driver.get(self.site_url)
        self.assertTrue("Plato" in driver.title)
        driver.find_element_by_class_name("octicon-mark-github").click()
        self.assertTrue("github.com" in driver.page_source)


    # def test_upload(self):
    #     driver = self.driver        
    #     driver.get(self.site_url)
    #     self.assertTrue("Plato" in driver.title)
    #     container = driver.find_element_by_class_name('container')
    #     assert container != None
    #     upload_file = driver.find_element_by_id("upload-file")
    #     assert upload_file != None
    #     upload_file.send_keys(os.getcwd() + r"\tests\empty.csv")
    #     strains = driver.find_elements_by_class_name('input-strain')
    #     assert len(strains) == 1, len(strains)
    #     strain = strains[0]
    #     assert strain.get_attribute('value') == '0', strain.get_attribute('value')
    #     assert strain.get_attribute('style') == 'background: rgb(255, 255, 255);', strain.get_attribute('style')
        

    # def test_download(self):
    #     driver = self.driver
    #     driver.get(self.site_url)
    #     btn = driver.find_element_by_class_name('octicon-arrow-down')
    #     assert btn != None
    #     btn.click()
    #     btn_download = self.driver.find_element_by_id('btnDownload')
    #     assert btn_download != None
    #     href = btn_download.get_attribute('href')
        
    #     script = """var x = new XMLHttpRequest();
    #     x.onload = function() {
    #         var div = document.createElement('div');
    #         div.id = 'test';
    #         div.innerText = x.responseText;
    #         document.body.appendChild(div)            
    #     };
    #     x.open('get', '%s');
    #     x.send();""" % href        
    #     driver.execute_script(script)
    #     test_div = driver.find_element_by_id('test')
    #     with open("tests/plate.csv") as f:
    #         plate_text = f.read()
    #     assert test_div.text == plate_text, tet_div.text


    def tearDown(self):        
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()