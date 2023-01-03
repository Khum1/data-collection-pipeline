from os import path, mkdir


class FileHandler():
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
        image_data = self.__get_cover_image(driver)
        path = f"raw_data/{self.isbn}/{self.isbn}.jpg"
        with open(path, 'wb') as handler:
            handler.write(image_data)
