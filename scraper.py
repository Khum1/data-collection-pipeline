from book import Book
from driver import Driver
from file_system_manager import FileManager
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Scraper:

    '''
    A class to navigate the Waterstones website and scrape url data for products. 

    Attributes
    ----------
    list_of_links : list
        list that will fill with links from products on the website

    Methods
    -------
    __get_website(url, driver):
        gets and displays the waterstones website in the thrillers section
    __accept_cookies(driver):
        finds the accept cookies button and clicks it
    __scroll(driver):
        scolls to the bottom of the webpage
    __click_show_more(driver):
        finds the "show more" button that will show more books on the page and clicks it
    __scroll_to_more_books(driver):
        scrolls to get 5 pages of books
    __get_list_of_links(driver):
        for each book on the page, finds the url for the product information

    '''
    def __init__(self):
        '''
        Constructs the objects necessary to scrape the website. 
        If being run from the scraper file, gets the website, accepts cookies, scrolls for more books and gets a list of product links.

        Parameters
        ----------
        driver : webdriver for Chrome
        '''

        if __name__ == "__main__":
            self.list_of_links = []
            logging.basicConfig(level=logging.INFO)
            logging.basicConfig(filename='app.log', filemode='w', format="%(name)s - %(levelname)s - %(message)s")
            initiallise_driver = Driver()
            driver = initiallise_driver.get_driver()
            url = 'https://www.waterstones.com/category/crime-thrillers-mystery/thrillers/format/17'
            self.load_website(url, driver)
            self.__scroll_to_more_books(driver)
            self.__get_list_of_links(driver)
            self.scrape_website()

    def __get_website(self, url, driver):
        '''
        gets and displays the waterstones website in the thrillers section

        Parameters
        ----------
        url : url to be scraped
        driver : webdriver for Chrome

        Returns
        -------
        None
        '''
        driver.get(url)

    def load_website(self, url, driver):
        self.__get_website(url, driver)
        self.__accept_cookies(driver)

    def __accept_cookies(self, driver):
        '''
        finds the accept cookies button and clicks it

        Parameters
        ----------
        driver : webdriver for Chrome

        Returns
        -------
        None
        '''
        sleep(2)
        accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies_button.click()

    
    def __scroll(self, driver):
        '''
        scolls to the bottom of the webpage

        Parameters
        ----------
        driver : webdriver for Chrome

        Returns
        -------
        None
        '''
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        sleep(3) #waits for books to load

    def __click_show_more(self, driver):
        '''
        finds the "show more" button that will show more books on the page and clicks it

        Parameters
        ----------
        driver : webdriver for Chrome

        Returns
        -------
        None
        '''
        show_more_section = driver.find_element(by=By.CLASS_NAME, value='infinite-load')
        show_more_button = show_more_section.find_element(by=By.XPATH, value='//*[@style="display: inline-block;"]')
        show_more_button.click()
        sleep(2) #waits for book to load

    def __scroll_to_more_books(self, driver):
        '''
        scrolls to get 5 pages of books (96 total)

        Parameters
        ----------
        driver : webdriver for Chrome

        Returns
        -------
        None
        '''
        self.__scroll(driver)
        logging.info("Scrolled once")
        self.__scroll(driver)
        logging.info("Scrolled twice")
        self.__scroll(driver)
        logging.info("Scrolled thrice")        
        driver.save_screenshot('screenshot.png') # Takes screenshot of the page to show that the page has scrolled
        self.__click_show_more(driver)
        self.__scroll(driver)

    def __get_list_of_links(self, driver):
        '''
        for each book on the page, finds the url for the product information

        Parameters
        ----------
        driver : webdriver for Chrome

        Returns
        -------
        None
        '''
        book_shelf = driver.find_element(by=By.CLASS_NAME, value='search-results-list')
        book_list = book_shelf.find_elements(by=By.XPATH, value='./div')

        for book in book_list:
            a_tag = book.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            self.list_of_links.append(link)

        logging.info(f'There are {len(self.list_of_links)} books on this page')

    def scrape_website(self):
        '''
        Scrapes the Waterstones website for book data and stores data in separate files

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        file_manager = FileManager()
        initialise_driver = Driver()
        driver = initialise_driver.get_driver()
        for url in self.list_of_links:
            driver.get(url)
            sleep(2)
            book = Book(driver)
            file_manager.create_dictionary_of_data(book)
            file_manager.create_product_folder()
            file_manager.store_data_to_json()
            file_manager.store_cover_image(driver)

scraper = Scraper()
