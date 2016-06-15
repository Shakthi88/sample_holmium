from holmium.core import TestCase, Page, Element, Elements,Locators, ElementMap,conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import unittest

# tests commot
class SeleniumHQPage(Page):
    
    nav_links = ElementMap(Locators.CSS_SELECTOR
        , "div#cssmenu ul>li"
        ,only_if=lambda element: element[0].is_displayed(),timeout=10
        , key=lambda element: element.find_element_by_css_selector("a").text
        , value=lambda element: element.find_element_by_css_selector("a")
    )
    
    jurnals = Elements(Locators.CLASS_NAME
                         ,'journal-content-article'                         
                         )
    
    nav_navigation_menu = ElementMap(Locators.CSS_SELECTOR
                                     ,"nav#navigation ul>li"
                                     , key=lambda element: element.find_element_by_tag_name("a").text
                                     , value=lambda element: element.find_element_by_tag_name("a")
                                     )
    
    nav_menu_elements = ElementMap(Locators.CSS_SELECTOR
        , "div#cssmenu ul>li"
        ,only_if=lambda element: element[0].is_displayed(),timeout=10
        , key=lambda element: element.find_element_by_css_selector("a").get_attribute('href')
        , value=lambda element: element.find_element_by_css_selector("a")
    )
    
    nav_menu = ElementMap(Locators.CSS_SELECTOR
        , "div#cssmenu ul>li"
        , key=lambda element: element.find_element_by_tag_name("a").text
        , value=lambda element: element.find_element_by_tag_name("a")
    )
    punch = Element(Locators.ID, 'punch')

    #header_text = Element(Locators.CSS_SELECTOR, "#mainContent>h2")

    def getSiteTagsById(self):
        e = WebDriverWait(self.driver, 30).until(
                                               Locators.CSS_SELECTOR
                                                , "div#cssmenu ul>li"
                                                , key=lambda element: element.find_element_by_tag_name("a").text
                                                , value=lambda element: element.find_element_by_tag_name("a")
                                                )
        return e   
    
class forumPage(Page):
    
    userNameField = Element(Locators.ID,"username")
    pwdField = Element(Locators.ID,"password")
    loginButton = Element(Locators.CLASS_NAME,"button1")  
    
class  forumLandingPage(Page):
        left_menu = ElementMap(Locators.CSS_SELECTOR
            , "div#page-header ul.linklist>li"
            ,only_if=lambda element: element[0].is_displayed(),timeout=10
            , key=lambda element: element.find_element_by_css_selector("a").text
            , value=lambda element: element.find_element_by_css_selector("a")
        )
