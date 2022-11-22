from selenium.webdriver.common.by import By
from json import dump as dump_data
import requests

class Book:
    def __init__(self, driver):
        self.create(driver)


    def create(self, driver):
        self.__get_title(driver)
        self.__get_author(driver)
        self.__get_isbn(driver)
        self.__get_rating(driver)
        self.__get_price(driver)
        self.__get_synopsis(driver)
        self.__get_number_of_pages(driver)

    def __get_title(self, driver):
        title = driver.find_element(by=By.XPATH, value='//*[@itemprop="name"]').text
        self.title = title

    def __get_price(self, driver):
        price = driver.find_element(by=By.XPATH, value='//*[@itemprop="price"]').text
        self.price = price
    
    def __get_author(self, driver):
        author = driver.find_element(by=By.XPATH, value='//*[@itemprop="author"]').text
        self.author =  author

    def __get_rating(self, driver):
        full_stars = driver.find_elements(by=By.XPATH, value='//*[@class="star-icon full"]') 
        half_star = []
        try:
            half_star.append(driver.find_element(by=By.XPATH, value='//*[@class="star-icon half"]'))
        except:
            pass
        rating = len(full_stars) + (len(half_star)/2)
        self.rating =  rating

    def __get_synopsis(self, driver):
        synopsis = ''
        description = driver.find_element(by=By.XPATH, value='//*[@id="scope_book_description"]')
        list_of_paragraphs = description.find_elements(by=By.TAG_NAME, value='p')
        for paragraph in list_of_paragraphs:
            synopsis += paragraph.get_attribute("innerText")
        self.synopsis = synopsis

    def __get_isbn(self, driver):
        isbn = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div/p/i[2]/span').text
        self.isbn =  isbn

    def __get_number_of_pages(self, driver):
        number_of_pages = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div/p/i[3]/span').text
        self.number_of_pages = number_of_pages

    def __create_dictionary_of_data(self) -> dict: 
        data = {
            'Title': self.title, 
            'Author': self.author, 
            'Rating': self.rating, 
            'Synopsis': self.synopsis, 
            'ISBN': self.isbn, 
            'Number of Pages': self.number_of_pages
        }
        return data

    def store_data_to_json(self):
        data = self.__create_dictionary_of_data()
        path = f"D:/Documents/GitHub/data-collection-pipeline/raw_data/{self.isbn}/data.json"
        with open(path, 'w', encoding='utf-8') as f:
            dump_data(data, f)
    
    def get_cover_image(self, driver):
        img_tag = driver.find_element(by=By.XPATH, value='//*[@id="scope_book_image"]')
        image_url = img_tag.get_attribute('src')
        image_data = requests.get(image_url).content
        path = f"D:/Documents/GitHub/data-collection-pipeline/raw_data/{self.isbn}/{self.isbn}.jpg"
        with open(path, 'wb') as handler:
            handler.write(image_data)