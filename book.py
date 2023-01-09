from retrieve_data import GetData

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
    '''
    def __init__(self, driver):
        self.__create_book(driver)
        '''
        Runs the create method which constructs the necessary attributes for the book object.

        Parameters
        ----------
        

        '''

    def __create_book(self, driver):
        '''
        creates an instance of the class by getting the title, author, isbn, rating, price, synopsis and number_of_pages from the webpage

        Parameters
        ----------
        None        
        Returns
        -------
        None
        '''
        self.get_data = GetData()
        self.get_data.title(driver)
        self.get_data.author(driver)
        self.get_data.isbn(driver)
        self.get_data.rating(driver)
        self.get_data.price(driver)
        self.get_data.synopsis(driver)
        self.get_data.number_of_pages(driver)
