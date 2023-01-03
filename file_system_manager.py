from retrieve_data import GetData
from json import dump as dump_data
from os import path, mkdir

class FileManager():
    '''
    A class for operating the system outside of the website and data

    Attributes
    ----------
    None

    Methods
    -------
    create_raw_data_folder()
        creates a folder to store the raw data from the website
    create_product_folder()
        creates a folder to store seperate product data from the website
    create_dictionary_of_data()
        creates a dictionary of the data for a book
    store_data_to_json()
        stores the book dictionary to a json file
    store_cover_image
        stores the cover image as a jpg file
    '''
    def __init__(self):
        self.create_raw_data_folder()
        
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
        dir_path = "raw_data"
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
        dir_path = f"raw_data/{book.isbn}"
        if not path.exists(dir_path):
            mkdir(dir_path)

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
        image_data = GetData.cover_image(driver)
        path = f"raw_data/{self.isbn}/{self.isbn}.jpg"
        with open(path, 'wb') as handler:
            handler.write(image_data)

    def create_dictionary_of_data(self) -> dict: 
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