from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.one_book = ''
        self.list_of_links = []

        if __name__ == "__main__":
            self.get_website()
            self.accept_cookies()
            self.scroll_to_more_books()
            self.get_list_of_links()


    def get_website(self):
        URL = 'https://www.waterstones.com/category/crime-thrillers-mystery/thrillers/page/1'
        self.driver.get(URL)

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
        self.one_book = self.driver.find_element(by=By.XPATH,value='//*[@data-productid="11647634"]')
        a_tag = self.one_book.find_element(by=By.TAG_NAME, value='a')
        link = a_tag.get_attribute('href')
        print(link)

    def get_price(self):
        price = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="price"]').text
        print(price)
    
    def get_author(self):
        author = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="author"]').text
        print(author)

    def get_rating(self):
        rating = self.driver.find_element(by=By.XPATH, value='//*[@class="star-rating"]').text #TODO find out how to make this work with coloured in stars
        print(rating)

    def get_synopsis(self):
        synopsis = self.driver.find_element(by=By.XPATH, value='//*[@class="two-columns"]').text #TODO make this work?
        print(synopsis)

    def get_cover_image(self):
        image = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="image"]')
        print(image)

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

    def scroll_to_more_books(self):
        scroll = self.scroll()
        time.sleep(1)
        scroll = self.scroll()
        time.sleep(1)
        scroll = self.scroll()
        time.sleep(1)
        show_more_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div[3]/button')
        show_more_button.click()
        time.sleep(2)
        scroll = self.scroll()
        time.sleep(1)

    def get_list_of_links(self):
        book_shelf = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div[2]')
        book_list = book_shelf.find_elements(by=By.XPATH, value='./div')

        for book in book_list:
            a_tag = book.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            self.list_of_links.append(link)

        print (f'There are {len(self.list_of_links)} books on this page')
        print(self.list_of_links)
        return self.list_of_links


def scrape():
    scraper = Scraper()
    for URL in scraper.list_of_links:
        scraper.driver.get(URL)
        time.sleep(1)
        scraper.get_price()
        scraper.get_author()
        scraper.get_synopsis()
        scraper.get_cover_image()



scrape()



