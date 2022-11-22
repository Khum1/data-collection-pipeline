from book import Book
from system import System
from selenium.webdriver.common.by import By
from time import sleep




class Scraper:
    def __init__(self, driver):
        self.list_of_links = []

        if __name__ == "__main__":
            self.__get_website(driver)
            self.__accept_cookies(driver)
            self.__get_list_of_links(driver)

    def __get_website(self, driver):
        URL = 'https://www.waterstones.com/category/crime-thrillers-mystery/thrillers/format/17'
        driver.get(URL)

    def __accept_cookies(self, driver):
        sleep(2)
        try:
            accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
        except:
            pass
    
    def __scroll(self, driver):
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        sleep(1)

    def __click_show_more(self, driver):
        show_more_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div[3]/button')
        show_more_button.click()
        sleep(2)

    def __scroll_to_more_books(self, driver):
        self.__scroll(driver)
        self.__scroll(driver)
        self.__scroll(driver)
        self.__click_show_more(driver)
        self.__scroll(driver)

    def __get_list_of_links(self, driver):
        book_shelf = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div[2]')
        book_list = book_shelf.find_elements(by=By.XPATH, value='./div')

        for book in book_list:
            a_tag = book.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            self.list_of_links.append(link)

        print (f'There are {len(self.list_of_links)} books on this page')


def scrape():
    system = System()
    scraper = Scraper(system.driver)
    system.create_raw_data_folder()

    for URL in scraper.list_of_links:
        system.driver.get(URL)
        sleep(2)

        book = Book(system.driver)
        system.create_product_folder(book)
        book.store_data_to_json()
        book.get_cover_image(system.driver)

scrape()