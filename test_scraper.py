from scraper import Scraper
from book import Book
from file_system_manager import FileManager
from selenium import webdriver
from driver import Driver
import unittest
from time import sleep
from os import path
from shutil import rmtree


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class ScraperTestCase(unittest.TestCase):

    def setUp(self):
        url = "https://www.waterstones.com/book/no-plan-b/lee-child/andrew-child/2928377082253"
        initialise_driver = Driver()
        driver = initialise_driver.get_driver()
        scraper = Scraper()
        scraper.load_website(url, driver)
        sleep(2)
        driver.get(url)
        sleep(2)
        self.file_manager = FileManager()
        book = Book(driver)
        self.file_manager.create_dictionary_of_data(book)
        self.file_manager.create_product_folder()
        self.file_manager.store_data_to_json()
        self.file_manager.store_cover_image(driver)
        self.driver = driver
        self.book = book


    def test_book_is_created(self):
        self.assertEqual(self.book.isbn, "2928377082253")
        self.assertNotEqual(self.book.price, 50)
        self.assertEqual(self.book.author, "Lee Child")

    def test_product_folder_created(self):
        dir_path = f"raw_data/{self.book.isbn}"
        self.assertTrue(path.exists(dir_path))

    def test_data_stored_as_json(self):
        dir_path = f"raw_data/{self.book.isbn}/data.json"
        self.assertTrue(path.exists(dir_path))

    def test_image_is_stored(self):
        dir_path = f"raw_data/{self.book.isbn}/{self.book.isbn}.jpg"
        self.assertTrue(path.exists(dir_path))

    def test_scraper(self):
        self.assertEqual(self.book.isbn, "2928377082253")
        self.assertNotEqual(self.book.price, 100)

        dir_path = f"raw_data/{self.book.isbn}"
        self.assertTrue(path.exists(dir_path))

        dir_path = f"raw_data/{self.book.isbn}/data.json"
        self.assertTrue(path.exists(dir_path))

        dir_path = f"raw_data/{self.book.isbn}/{self.book.isbn}.jpg"
        self.assertTrue(path.exists(dir_path))

    def remove_product_dir(self):
        dir_path = f"raw_data/{self.book.isbn}"
        if path.exists(dir_path):
            rmtree(f"raw_data/{self.book.isbn}")

    def tearDown(self):
        self.driver.quit()
        self.remove_product_dir()
        del self.book

        
unittest.main(argv=[''], verbosity=0, exit=False)
