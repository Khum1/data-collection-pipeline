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
        GetData.title(driver)
        GetData.author(driver)
        GetData.isbn(driver)
        GetData.rating(driver)
        GetData.price(driver)
        GetData.synopsis(driver)
        GetData.number_of_pages(driver)
