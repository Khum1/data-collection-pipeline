from scraper import Scraper
from book import Book
from file_system_manager import System
from selenium import webdriver
import unittest
from time import sleep
from os import path
from shutil import rmtree


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class ScraperTestCase(unittest.TestCase):

    

    def setUp(self):
        url = "https://www.waterstones.com/book/no-plan-b/lee-child/andrew-child/2928377082253"
        self.driver = driver = webdriver.Chrome(options=options)
        scraper = Scraper(driver)
        scraper.load_website(driver)
        sleep(2)
        driver.get(url)
        sleep(2)

        self.book = Book(driver)
        self.system = System()
        self.system.create_raw_data_folder()

    def test_website_creates_book(self):
        self.assertEqual(self.book.isbn, "2928377082253")
        self.assertNotEqual(self.book.price, 50)
        self.assertEqual(self.book.author, "Lee Child")

    def test_scraper(self):
        self.assertEqual(self.book.isbn, "2928377082253")
        self.assertNotEqual(self.book.price, 100)

        self.system.create_product_folder(self.book)
        dir_path = f"raw_data/{self.book.isbn}"
        self.assertTrue(path.exists(dir_path))

        self.book.store_data_to_json()
        dir_path = f"raw_data/{self.book.isbn}/data.json"
        self.assertTrue(path.exists(dir_path))

        self.book.store_cover_image(self.driver)
        dir_path = f"raw_data/{self.book.isbn}/{self.book.isbn}.jpg"
        self.assertTrue(path.exists(dir_path))

    def tearDown(self):
        self.driver.quit()
        self.remove_product_dir()
        del self.book
        del self.system

    def remove_product_dir(self):
        dir_path = f"raw_data/{self.book.isbn}"
        if path.exists(dir_path):
            rmtree(f"raw_data/{self.book.isbn}")
        
unittest.main(argv=[''], verbosity=0, exit=False)
