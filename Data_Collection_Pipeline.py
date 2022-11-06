from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Scraper:
    def __init__(self):
        self.URL = 'https://www.waterstones.com/category/crime-thrillers-mystery/thrillers/page/1'
        self.driver = webdriver.Chrome()
        self.book = ''


    def get_website(self):
        self.driver.get(self.URL)

    def accept_cookies(self):
        time.sleep(2)
        try:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
        except AttributeError:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()

        except:
            pass

    def get_link(self):
        time.sleep(2)
        self.book = self.driver.find_element(by=By.XPATH,\
            value='//*[@data-productid="11647634"]')
        a_tag = self.book.find_element(by=By.TAG_NAME, value='a')
        link = a_tag.get_attribute('href')
        print(link)

    def get_price(self):
        price = self.driver.find_element(by=By.XPATH, value='//*[@id="p_11647634"]/div/div[2]/div[2]/span[3]').text
        print(price)
    
    def get_author(self):
        author = self.driver.find_element(by=By.XPATH, value='//*[@id="p_11647634"]/div/div[2]/span/a/b').text
        print(author)

    def get_rating(self):
        rating = self.driver.find_element(by=By.XPATH, value='//*[@id="p_11647634"]/div/div[2]/div[3]').text
        print(rating)

    
def scrape():
    scraper = Scraper()
    scraper.get_website()
    scraper.accept_cookies()
    scraper.get_link()
    scraper.get_price()
    scraper.get_author()
    scraper.get_rating()


scrape()


