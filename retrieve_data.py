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
    title(driver)
        gets the title of the book
    author(driver)
        gets the author of the book
    isbn(driver)
        gets the unique ISBN number of the book
    rating(driver)
        gets the rating of the book
    price(driver)
        gets the price of the book
    synopsis(driver)
        gets the synopsis of the book
    number_of_pages(driver)
        gets the number of pages that the book has
    cover_image(driver)
        gets the cover image for the book
    '''

    def title(self, driver) -> str:
        '''
        gets the title of the book

        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        title = driver.find_element(by=By.XPATH, value="//*[@id='scope_book_title']").text
        return title

    def price(self, driver):
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
        return price
    
    def author(self, driver):
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
        return author

    def rating(self, driver):
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
            full_stars = driver.find_elements(by=By.XPATH, value='//*[@class="star-icon full"]')
        except NoSuchElementException:
            rating = 0
        try:
            driver.find_element(by=By.XPATH, value='//*[@class="star-icon half"]')
            half_star = 0.5
        except NoSuchElementException:
            half_star = 0
        rating = len(full_stars) + half_star

        return rating

    def synopsis(self, driver):
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
        return synopsis

    def isbn(self, driver):
        '''
        gets the unique ISBN of the book
        
        Parameters
        ----------
        driver : webdriver for Chrome
        
        Returns
        -------
        None
        '''
        isbn = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[2]/section[2]/div[2]/div[1]/div[1]/p/i[2]/span').text
        return isbn

    def number_of_pages(self, driver):
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
        return number_of_pages

    def cover_image(self, driver):
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
