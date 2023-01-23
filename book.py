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
        get_data = GetData()
        title = get_data.title(driver)
        author = get_data.author(driver)
        isbn = get_data.isbn(driver)
        rating = get_data.rating(driver)
        price = get_data.price(driver)
        synopsis = get_data.synopsis(driver)
        number_of_pages = get_data.number_of_pages(driver)
        
        return title, author, isbn, rating, price, synopsis, number_of_pages
