from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import json
import requests



options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
books_dicts = []

class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.list_of_links = []
        self.isbn = ''


        if __name__ == "__main__":
            self.get_website()
            self.accept_cookies()
            self.scroll_to_more_books()
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

    def scroll_to_more_books(self):
        # self.scroll()
        # self.scroll()
        # self.scroll()
        # self.click_show_more()
        # self.scroll()
        pass

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

    def get_title(self):
        title = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="name"]').text
        return title

    def get_price(self):
        price = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="price"]').text
        return price
    
    def get_author(self):
        author = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="author"]').text
        return author

    def get_rating(self):
        full_stars = self.driver.find_elements(by=By.XPATH, value='//*[@class="star-icon full"]') 
        half_star = []
        try:
            half_star.append(self.driver.find_element(by=By.XPATH, value='//*[@class="star-icon half"]'))
        except:
            pass
        rating = len(full_stars) + (len(half_star)/2)
        return rating

    def get_isbn(self):
        isbn = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div/p/i[2]/span').text
        return isbn

    def get_synopsis(self): #TODO make this work?
        synopsis = ''
        description = self.driver.find_element(by=By.XPATH, value='//*[@id="scope_book_description"]')
        list_of_paragraphs = description.find_elements(by=By.TAG_NAME, value='p')
        for paragraph in list_of_paragraphs:
            synopsis += paragraph.text
        print(synopsis)
        

    def get_number_of_pages(self):
        number_of_pages = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div/p/i[3]/span').text
        return number_of_pages

    def get_all_text_data(self):
        title = self.get_title()
        author = self.get_author()
        rating = self.get_rating()
        synopsis = self.get_synopsis()
        self.isbn = self.get_isbn()
        number_of_pages = self.get_number_of_pages()
        #books_dicts.append({'Title': title, 'Author': author, 'Rating': rating, 'Synopsis': synopsis, 'ISBN': isbn, 'Number of Pages': number_of_pages})
        self.create_product_folder()
        data = {'Title': title, 'Author': author, 'Rating': rating, 'Synopsis': synopsis, 'ISBN': self.isbn, 'Number of Pages': number_of_pages}
        self.create_json(data)

    def get_cover_image(self):
        img_tag = self.driver.find_element(by=By.XPATH, value='//*[@id="scope_book_image"]')
        image_url = img_tag.get_attribute('src')
        image_data = requests.get(image_url).content
        with open(f'D:/Documents/GitHub/data-collection-pipeline/raw_data/{self.isbn}/{self.isbn}.jpg', 'wb') as handler:
            handler.write(image_data)
        

    def create_raw_data_folder(self):
        if not os.path.exists('D:/Documents/GitHub/data-collection-pipeline/raw_data'):
            os.mkdir('D:/Documents/GitHub/data-collection-pipeline/raw_data')

    def create_product_folder(self):
        os.mkdir(f'D:/Documents/GitHub/data-collection-pipeline/raw_data/{self.isbn}')

    def create_json(self, data):
        with open(f'D:/Documents/GitHub/data-collection-pipeline/raw_data/{self.isbn}/data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)


def scrape():
    scraper = Scraper()
    for URL in scraper.list_of_links:
        scraper.driver.get(URL)
        time.sleep(1)
        # scraper.create_raw_data_folder()
        # scraper.get_all_text_data()
        # scraper.get_cover_image()
        scraper.get_synopsis()
    print(books_dicts)


scrape()
