from os import path, mkdir
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chromeOptions = Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--window-size=1920,1080")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
chromeOptions.add_argument(f'user-agent={user_agent}')
# options = webdriver.ChromeOptions() 
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# s = Service('/data-collection/pipeline')


class System():
    '''
    A class for operating the system outside of the website and data

    Attributes
    ----------
    driver : webdriver for Chrome

    Methods
    -------
    create_raw_data_folder()
        creates a folder to store the raw data from the website
    create_product_folder()
        creates a folder to store seperate product data from the website
    '''
    def __init__(self):
        '''
        Initiallises the driver for use.

        Parameters
        ----------
        None
        '''
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        
    def create_raw_data_folder(self):
        '''
        creates a folder to store the raw data from the website

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        dir_path = "D:/Documents/GitHub/data-collection-pipeline/raw_data"
        if not path.exists(dir_path):
            mkdir(dir_path)

    def create_product_folder(self, book):
        '''
        creates a folder to store seperate product data from the website

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        dir_path = f"D:/Documents/GitHub/data-collection-pipeline/raw_data/{book.isbn}"
        if not path.exists(dir_path):
            mkdir(dir_path)
