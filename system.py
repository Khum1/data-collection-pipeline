from selenium import webdriver
from os import path, mkdir

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

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
        self.driver = webdriver.Chrome(options=options)
        
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

