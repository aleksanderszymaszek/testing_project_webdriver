import unittest
from webdriverplus import WebDriver
from Common.Helpers.SeleniumHelper_webdriver import *


class SeleniumTestCasesWebdriver(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.url = "http://goal.com/en"
            cls.verificationErrors = []
            cls.browser = WebDriver('firefox')
            SeleniumHelper.browser = cls.browser

        @classmethod
        def tearDownClass(cls):
            cls.browser.quit()
            assert([] == cls.verificationErrors)

            # this is a test four from the excersises
        def test_one(self):

            adress = "http://book.theautomatedtester.co.uk/chapter1"
            radio = "xpath=.//*[@id='radiobutton']"
            select = "xpath=//*[@id='selecttype']"

            SeleniumHelper.open(adress)
            SeleniumHelper.window_maximize()
            SeleniumHelper.wait_for_page_to_load(300000)
            SeleniumHelper.wait_for_element_present(radio)
            SeleniumHelper.click(radio)
            SeleniumHelper.wait_for_element_present(select)
            SeleniumHelper.verify_element_present(select)
            SeleniumHelper.select("#selecttype", "Selenium RC")
            SeleniumHelper.verify_element_present("xpath=//*[@id='divontheleft']")
            SeleniumHelper.click("xpath=//*[@id='secondajaxbutton']")
            SeleniumHelper.wait_for_element_present("xpath=.//*[@id='html5div']/div")
            SeleniumHelper.verify_text_present("I have been added with a timeout")
            SeleniumHelper.click("xpath=//*[@id='loadajax']")
            SeleniumHelper.wait_for_element_present("xpath=//*[@id='ajaxdiv']/p")
            SeleniumHelper.click("xpath=//*[@id='html5div']")
            SeleniumHelper.type("#html5div", "some text")

            # this is a test three for the excersises
        def test_two(self):

            adress = "http://www.goal.com/en-gb/"
            module = "xpath=//*[@class='module module-topstories']"
            top = "xpath=//*[@class='widget-header']/h2[.='Top Stories']"
            content = "xpath=//*[@class='top-story']//*[@class='content']//a"

            SeleniumHelper.open(adress)
            SeleniumHelper.window_maximize()
            SeleniumHelper.wait_for_page_to_load(300000)
            SeleniumHelper.wait_for_element_present(module)
            SeleniumHelper.verify_element_present(module)
            SeleniumHelper.wait_for_element_present(top)
            SeleniumHelper.verify_element_present(top)
            SeleniumHelper.verify_element_present("xpath=//*[@class='top-story']/a/img")
            SeleniumHelper.wait_for_element_present(content)
            SeleniumHelper.verify_element_present(content)
            # SeleniumHelper.verify_element_present_and_not_empty(content)
            SeleniumHelper.verify_element_present("xpath=(//span[@class='comment-ico img-rep'])[1]")
            SeleniumHelper.verify_element_present("xpath=//*[@id='unique-shareicon-30']")
            count = SeleniumHelper.get_count(".top-story>.story")

        # this is a test one from the excersises
        def test_three(self):

            SeleniumHelper.open("http://www.goal.com/en-gb/")
            SeleniumHelper.window_maximize()
            SeleniumHelper.wait_for_page_to_load(300000)
            SeleniumHelper.wait_for_element_present("xpath=//*[@class='featured-stories']")
            SeleniumHelper.click("xpath=(//*[@class='featured-stories']//*[@class='story']/h3/a)[1]")
            SeleniumHelper.wait_for_page_to_load(300000)

        def test_four(self):

            SeleniumHelper.open("http://www.toolsqa.com/automation-practice-form/")
            SeleniumHelper.window_maximize()
            SeleniumHelper.wait_for_page_to_load(300000)
            SeleniumHelper.wait_for_element_present("xpath=//*[@id='continents']")
            SeleniumHelper.verify_element_present("xpath=//*[@id='continents']")
            SeleniumHelper.select("#continents", "Africa")


        if __name__ == "__main__":
            unittest.main(verbosity=4)
