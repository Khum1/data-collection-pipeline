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
    def __init__(self):
        self.get_data = GetData
        self.__create_book()
        '''
        Runs the create method which constructs the necessary attributes for the book object.

        Parameters
        ----------
        

        '''

    def __create_book(self):
        '''
        creates an instance of the class by getting the title, author, isbn, rating, price, synopsis and number_of_pages from the webpage

        Parameters
        ----------
        None        
        Returns
        -------
        None
        '''
        self.get_data.title()
        self.get_data.author()
        self.get_data.isbn()
        self.get_data.rating()
        self.get_data.price()
        self.get_data.synopsis()
        self.get_data.number_of_pages()
