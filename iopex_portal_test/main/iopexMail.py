from holmium.core import TestCase, Page, Element, Locators, ElementMap
from selenium import webdriver
import unittest

from holmium_obj import SeleniumHQPage, forumPage, forumLandingPage

class SeleniumHQTest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = SeleniumHQPage(self.driver, "https://myportal.iopex.com/en/group/iopex-chennai/home")
        
    def test_header_links(self):
        print self.driver.current_url , "=== ", len(self.page.nav_links), self.page.nav_links
        #self.assertTrue(len(self.page.nav_links) == 5)
        self.page.nav_links['HR'].click()        
        self.page = SeleniumHQPage(self.driver)
        print 'Menu ==>', self.page.nav_links #self.page.nav_menu_elements
        self.page.jurnals[0].click()
        #self.page.nav_menu_elements['https://myportal.iopex.com/en/group/iopex-chennai/hrms'].click()
        
        for handle in self.driver.window_handles:
            print handle
            self.driver.switch_to_window(handle)
        #self.driver.switch_to_window("_blank")
        print "-====", self.driver.current_url
        
        self.forum_page = forumPage(self.driver)
        self.forum_page.userNameField.send_keys('nissan.dhanabal')
        self.forum_page.pwdField.send_keys('shakthi@88')
        self.forum_page.loginButton.click()
        
        
        self.landingPage = forumLandingPage(self.driver)
        print self.landingPage.left_menu
        
        
            
    '''       
    def test_header_meanu(self):
        self.assertFalse(
            "Homesssss" 
            in sorted(self.page.nav_links.keys()))
        print "================"        
           

    def test_click_home(self):  
        self.page.nav_links['Home'].click()   
        #self.page.punch.click()
        
    def test_click_hr(self):
        self.page.nav_links["HR"].click()
        
    def test_click_menu(self):
        self.page.nav_navigation_menu['iOPEX Gallery'].click()
        self.page.nav_navigation_menu['Home'].click()
      
     
          
    def test_nave_elements(self):
        print self.page.nav_menu_elements
        for element in self.page.nav_menu_elements:
            pass#element.click()
    '''

    
        
if __name__ == '__main__':   
    unittest.main()     
        