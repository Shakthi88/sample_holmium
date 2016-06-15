from holmium.core import TestCase, Page, Element, Locators, ElementMap
import unittest


class SeleniumHQPage(Page):
    nav_links = ElementMap(Locators.CSS_SELECTOR
        , "div#header ul>li"
        , key=lambda element: element.find_element_by_tag_name("a").text
        , value=lambda element: element.find_element_by_tag_name("a")
    )
        

    header_text = Element(Locators.CSS_SELECTOR, "#mainContent>h2")
    
    



class SeleniumHQTest(TestCase):
    
    def setUp(self):
        print 'setup called -->'
        self.page = SeleniumHQPage(self.driver, "http://seleniumhq.org")

    def test_header_links(self):
        self.assertTrue(len(self.page.nav_links) > 0)
        self.assertElementsDisplayed(self.page.nav_links)
        self.assertEquals(
            sorted(
                ["Projects", "Download", "Documentation", "Support", "About"]
            )
            , sorted(self.page.nav_links.keys()))

    def test_about_selenium_heading(self):
        self.page.nav_links["About"].click()
        self.assertElementTextEqual(self.page.header_text, "About Selenium")
