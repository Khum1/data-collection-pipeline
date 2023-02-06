from retrieve_data import GetData

class Book:
    '''
    A class to represent a book

    Attributes
    ----------
    None

    Methods
    -------
    __create_book(driver)
        creates an instance of the class by getting the title, author, isbn, rating, price, synopsis and number_of_pages from the webpage
    '''
    def __init__(self, driver):
        self.__create_book(driver)
        '''
        Runs the create method which constructs the necessary attributes for the book object.

        Parameters
        ----------
        driver : webdriver for chrome
        
        '''
    def __create_book(self, driver):
        '''
        creates an instance of the class by getting the title, author, isbn, rating, price, synopsis and number_of_pages from the webpage
        Parameters
        ----------
        driver : webdriver for chrome

        Returns
        -------
        None
        '''
        get_data = GetData()
        self.title = get_data.title(driver)
        self.author = get_data.author(driver)
        self.isbn = get_data.isbn(driver)
        self.rating = get_data.rating(driver)
        self.price = get_data.price(driver)
        self.synopsis = get_data.synopsis(driver)
        self.number_of_pages = get_data.number_of_pages(driver)