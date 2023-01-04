from driver import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests

class GetData:
    '''
    Class to find and retrieve data from a website
    Attributes
    ----------
    None

    Methods
    -------
    title()
        gets the title of the book
    author()
        gets the author of the book
    isbn()
        gets the unique ISBN number of the book
    rating()
        gets the rating of the book
    price()
        gets the price of the book
    synopsis()
        gets the synopsis of the book
    number_of_pages()
        gets the number of pages that the book has
    cover_image()
        gets the cover image for the book
    '''

    def __init__(self):
        self.driver = Driver.get_driver()
        
    def title(self) -> str:
        '''
        gets the title of the book

        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        title = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="name"]').text
        self.title = title

    def price(self):
        '''
        gets the price of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        price = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="price"]').text
        self.price = price
    
    def author(self):
        '''
        gets the author of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        author = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="author"]').text
        self.author =  author

    def rating(self):
        '''
        gets the rating of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        try:
            full_stars = self.driver.find_elements(by=By.XPATH, value='//*[@class="star-icon full"]')
        except NoSuchElementException:
            rating = 0
        try:
            self.driver.find_element(by=By.XPATH, value='//*[@class="star-icon half"]')
            half_star = 0.5
        except NoSuchElementException:
            half_star = 0
        rating = len(full_stars) + half_star

        self.rating =  rating

    def synopsis(self):
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
        description = self.driver.find_element(by=By.XPATH, value='//*[@id="scope_book_description"]')
        list_of_paragraphs = description.find_elements(by=By.TAG_NAME, value='p')
        for paragraph in list_of_paragraphs:
            synopsis += paragraph.get_attribute("innerText")
        self.synopsis = synopsis

    def isbn(self):
        '''
        gets the unique ISBN number of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        isbn = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div[1]/p/i[2]/span').text
        self.isbn =  isbn

    def number_of_pages(self):
        '''
        gets the number of pages that the book has
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        number_of_pages = self.driver.find_element(by=By.XPATH, value='//*[@itemprop="numberOfPages"]').text
        self.number_of_pages = number_of_pages

    def cover_image(self):
        '''
        gets the cover image for the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        image_data (bytes): cover image of the book
        '''
        img_tag = self.driver.find_element(by=By.XPATH, value='//*[@id="scope_book_image"]')
        image_url = img_tag.get_attribute('src')
        image_data = requests.get(image_url).content
        return image_data
