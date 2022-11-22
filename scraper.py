from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import json
import requests

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])


class Scraper:
    def __init__(self, system):
        self.driver = system.driver
        self.list_of_links = []

        if __name__ == "__main__":
            self.get_website()
            self.accept_cookies()
            self.get_list_of_links()

    def get_website(self):
        URL = 'https://www.waterstones.com/category/crime-thrillers-mystery/thrillers/format/17'
        self.driver.get(URL)

    def accept_cookies(self):
        time.sleep(2)
        try:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
        except:
            pass
    
    def scroll(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        time.sleep(1)

    def click_show_more(self):
        show_more_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div[3]/button')
        show_more_button.click()
        time.sleep(2)

    def get_list_of_links(self):
        book_shelf = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div[2]')
        book_list = book_shelf.find_elements(by=By.XPATH, value='./div')

        for book in book_list:
            a_tag = book.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            self.list_of_links.append(link)

        print (f'There are {len(self.list_of_links)} books on this page')


class System():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        
    def create_raw_data_folder(self):
        path = "D:/Documents/GitHub/data-collection-pipeline/raw_data"
        if not os.path.exists(path):
            os.mkdir(path)

    def create_product_folder(self, book):
        path = f"D:/Documents/GitHub/data-collection-pipeline/raw_data/{book.isbn}"
        if not os.path.exists(path):
            os.mkdir(path)



class Book:
    def __init__(self, system):
        self.driver = system.driver
        self.create()

    def create(self):
        self.get_title()
        self.get_author()
        self.get_isbn()
        self.get_rating()
        self.get_price()
        self.get_synopsis()
        self.get_number_of_pages()

    def get_title(self):
        title = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="name"]').text
        self.title = title

    def get_price(self):
        price = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="price"]').text
        self.price = price
    
    def get_author(self):
        author = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="author"]').text
        self.author =  author

    def get_rating(self):
        full_stars = self.driver.find_elements(by=By.XPATH, value='//*[@class="star-icon full"]') 
        half_star = []
        try:
            half_star.append(self.driver.find_element(by=By.XPATH, value='//*[@class="star-icon half"]'))
        except:
            pass
        rating = len(full_stars) + (len(half_star)/2)
        self.rating =  rating

    def get_isbn(self):
        isbn = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div/p/i[2]/span').text
        self.isbn =  isbn

    def get_number_of_pages(self):
        number_of_pages = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div/p/i[3]/span').text
        self.number_of_pages = number_of_pages

    def get_synopsis(self): #TODO make this work?
        # synopsis = self.driver.find_elements(by=By.XPATH, value='//*[class="tab-content content-text tab-content-synopsis active"]').text
        self.synopsis = ""

    def store_to_json(self):
        data = {
            'Title': self.title, 
            'Author': self.author, 
            'Rating': self.rating, 
            'Synopsis': self.synopsis, 
            'ISBN': self.isbn, 
            'Number of Pages': self.number_of_pages
        }

        path = f"D:/Documents/GitHub/data-collection-pipeline/raw_data/{self.isbn}/data.json"
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    
    def get_cover_image(self):
        img_tag = self.driver.find_element(by=By.XPATH, value='//*[@id="scope_book_image"]')
        image_url = img_tag.get_attribute('src')
        image_data = requests.get(image_url).content
        path = f"D:/Documents/GitHub/data-collection-pipeline/raw_data/{self.isbn}/{self.isbn}.jpg"
        with open(path, 'wb') as handler:
            handler.write(image_data)


def scrape():
    system = System()
    scraper = Scraper(system)
    system.create_raw_data_folder()

    for URL in scraper.list_of_links:
        scraper.driver.get(URL)
        time.sleep(2)

        book = Book(system)
        system.create_product_folder(book)
        book.store_to_json()
        book.get_cover_image()

scrape()