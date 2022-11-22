from selenium import webdriver
from os import path, mkdir

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class System():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        
    def create_raw_data_folder(self):
        dir_path = "D:/Documents/GitHub/data-collection-pipeline/raw_data"
        if not path.exists(dir_path):
            mkdir(dir_path)

    def create_product_folder(self, book):
        dir_path = f"D:/Documents/GitHub/data-collection-pipeline/raw_data/{book.isbn}"
        if not path.exists(dir_path):
            mkdir(dir_path)

