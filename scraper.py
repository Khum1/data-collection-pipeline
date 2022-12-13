from book import Book
from system import System
from selenium.webdriver.common.by import By
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
    __get_website():
        gets and displays the waterstones website in the thrillers section
    __accept_cookies():
        finds the accept cookies button and clicks it
    __scroll():
        scolls to the bottom of the webpage
    __click_show_more():
        finds the "show more" button that will show more books on the page and clicks it
    __scroll_to_more_books():
        scrolls to get 5 pages of books (96 total)
    __get_list_of_links():
        for each book on the page, finds the url for the product information

    '''
    def __init__(self, driver):
        '''
        Constructs the objects necessary to scrape the website. 
        If being run from the scraper file, gets the website, accepts cookies, scrolls for more books and gets a list of product links.

        Parameters
        ----------
        driver : webdriver for Chrome
        '''
        self.list_of_links = []

        if __name__ == "__main__":
            self.load_website(driver)
            # self.__scroll_to_more_books(driver)
            self.__get_list_of_links(driver)

    def __get_website(self, driver):
        '''
        gets and displays the waterstones website in the thrillers section

        Parameters
        ----------
        driver : webdriver for Chrome

        Returns
        -------
        None
        '''
        URL = 'https://www.waterstones.com/category/crime-thrillers-mystery/thrillers/format/17'
        driver.get(URL)

    def load_website(self, driver):
        self.__get_website(driver)
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
        try:
            accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
        except:
            pass
    
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
        sleep(3)

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
        show_more_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[3]/div[3]/button')
        show_more_button.click()
        sleep(2)

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
        self.__scroll(driver)
        self.__scroll(driver)
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
        book_shelf = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[3]/div[2]')
        book_list = book_shelf.find_elements(by=By.XPATH, value='./div')

        for book in book_list:
            a_tag = book.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            self.list_of_links.append(link)

        print (f'There are {len(self.list_of_links)} books on this page')


def scrape():
    '''
    Scrapes the Waterstones website for book data and stores data in separate files

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    system = System()
    scraper = Scraper(system.driver)
    system.create_raw_data_folder()

    for URL in scraper.list_of_links:
        system.driver.get(URL)
        sleep(2)

        book = Book(system.driver)
        system.create_product_folder(book)
        book.store_data_to_json()
        book.store_cover_image(system.driver)

scrape()