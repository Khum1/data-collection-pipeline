from json import dump as dump_data
from selenium.webdriver.common.by import By
import requests

class Book:
    '''
    A class to represent a book

    Attributes
    ----------
    None

    Methods
    -------
    __create()
        creates an instance of the class by getting the title, author, isbn, rating, price, synopsis and number_of_pages from the webpage
    __get_title()
        gets the title of the book
    __get_author()
        gets the author of the book
    __get_isbn()
        gets the unique ISBN number of the book
    __get_rating()
        gets the rating of the book
    __get_price()
        gets the price of the book
    __get_synopsis()
        gets the synopsis of the book
    __get_number_of_pages()
        gets the number of pages that the book has
    __create_dictionary_of_data()
        creates a dictionary of the data for this instance of the book
    store_data_to_json()
        stores the book dictionary to a json file
    get_cover_image()
        gets the cover image for the book
    store_cover_image
        stores the cover image as a jpg file
    '''
    def __init__(self, driver):
        self.__create_book(driver)
        '''
        Runs the create method which constructs the necessary attributes for the book object.

        Parameters
        ----------
        driver : webdriver for Chrome

        '''

    def __create_book(self, driver):
        '''
        creates an instance of the class by getting the title, author, isbn, rating, price, synopsis and number_of_pages from the webpage

        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        self.__get_title(driver)
        self.__get_author(driver)
        self.__get_isbn(driver)
        self.__get_rating(driver)
        self.__get_price(driver)
        self.__get_synopsis(driver)
        self.__get_number_of_pages(driver)

    def __get_title(self, driver) -> str:
        '''
        gets the title of the book

        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        title = driver.find_element(by=By.XPATH, value='//*[@itemprop="name"]').text
        self.title = title

    def __get_price(self, driver):
        '''
        gets the price of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        price = driver.find_element(by=By.XPATH, value='//*[@itemprop="price"]').text
        self.price = price
    
    def __get_author(self, driver):
        '''
        gets the author of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        author = driver.find_element(by=By.XPATH, value='//*[@itemprop="author"]').text
        self.author =  author

    def __get_rating(self, driver):
        '''
        gets the rating of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        full_stars = driver.find_elements(by=By.XPATH, value='//*[@class="star-icon full"]') 
        half_star = []
        try:
            half_star.append(driver.find_element(by=By.XPATH, value='//*[@class="star-icon half"]'))
        except:
            pass
        rating = len(full_stars) + (len(half_star)/2)
        self.rating =  rating

    def __get_synopsis(self, driver):
        '''
        gets the synopsis of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        synopsis = ''
        description = driver.find_element(by=By.XPATH, value='//*[@id="scope_book_description"]')
        list_of_paragraphs = description.find_elements(by=By.TAG_NAME, value='p')
        for paragraph in list_of_paragraphs:
            synopsis += paragraph.get_attribute("innerText")
        self.synopsis = synopsis

    def __get_isbn(self, driver):
        '''
        gets the unique ISBN number of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        isbn = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[2]/section[2]/div[2]/div[1]/div[1]/p/i[2]/span').text
        self.isbn =  isbn

    def __get_number_of_pages(self, driver):
        '''
        gets the number of pages that the book has
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        number_of_pages = driver.find_element(by=By.XPATH, value='//*[@itemprop="numberOfPages"]').text
        self.number_of_pages = number_of_pages

    def __create_dictionary_of_data(self) -> dict: 
        '''
        creates a dictionary of the data for this instance of the book
        
        Parameters
        ----------
        None
        
        Returns
        -------
        data (dict): Dictionary of data from the webpage about this instance of the book
        '''
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
        '''
        stores the book dictionary to a json file
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        '''
        data = self.__create_dictionary_of_data()
        path = f"raw_data/{self.isbn}/data.json"
        with open(path, 'w', encoding='utf-8') as f:
            dump_data(data, f)
    
    def __get_cover_image(self, driver):
        '''
        gets the cover image for the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        image_data (bytes): cover image of the book
        '''
        img_tag = driver.find_element(by=By.XPATH, value='//*[@id="scope_book_image"]')
        image_url = img_tag.get_attribute('src')
        image_data = requests.get(image_url).content
        return image_data
        
    
    def store_cover_image(self, driver):
        '''
        stores the cover image as a jpg file
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        image_data = self.__get_cover_image(driver)
        path = f"D:/Documents/GitHub/data-collection-pipeline/raw_data/{self.isbn}/{self.isbn}.jpg"
        with open(path, 'wb') as handler:
            handler.write(image_data)