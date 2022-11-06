from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Scraper:
    def __init__(self):
        self.URL = 'https://www.waterstones.com/category/crime-thrillers-mystery/thrillers'
        self.driver = webdriver.Chrome()


    def get_website(self):
        self.driver.get(self.URL)
        time.sleep(2)

    def accept_cookies(self):
        try:
            self.driver.switch_to_frame('onetrust-policy-text')
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
        except AttributeError:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
            time.sleep(2)
        except:
            pass

    

