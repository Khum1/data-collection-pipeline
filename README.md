# Data Collection Pipeline

In this project I have...

**Technologies used:**

- Python
- Selenium - used to perform simple functions within the web browser to navigate the website.

## Milestone 1/2

I set up my github repo and chose the website I would be scraping. I chose Waterstones and will be focussing on the Thrillers section of the site 

## Milestone 3

I have built the Scraper class which allows the user to get_website() and accept_cookies(). Following this it scrolls to the bottom of the page and clicks a "See More" button and prints "There are {96} books on this page". It then copies the link for each book into a list_of_links and prints the list. At this stage, I have also extracted data from the first book in the list, such as price, author and star rating and plan to follow this into the next milestone.

``` python

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class Scraper:
    def __init__(self):
        self.URL = 'https://www.waterstones.com/category/crime-thrillers-mystery/thrillers/page/1'
        self.driver = webdriver.Chrome(options=options)
        self.one_book = ''

        if __name__ == "__main__":
            self.get_website()
            self.accept_cookies()
            self.get_link()
            self.get_price()
            self.get_author()
            self.get_rating()
            self.scroll_to_more_books()
            self.get_list_of_links()
            self.scroll()


    def get_website(self):
        self.driver.get(self.URL)

    def accept_cookies(self):
        time.sleep(2)
        try:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
        except AttributeError:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()

        except:
            pass

    def get_link(self):
        time.sleep(2)
        self.one_book = self.driver.find_element(by=By.XPATH,value='//*[@data-productid="11647634"]')
        a_tag = self.one_book.find_element(by=By.TAG_NAME, value='a')
        link = a_tag.get_attribute('href')
        print(link)

    def get_price(self):
        price = self.driver.find_element(by=By.XPATH, value='//*[@id="p_11647634"]/div/div[2]/div[2]/span[3]').text
        print(price)
    
    def get_author(self):
        author = self.driver.find_element(by=By.XPATH, value='//*[@id="p_11647634"]/div/div[2]/span/a/b').text
        print(author)

    def get_rating(self):
        rating = self.driver.find_element(by=By.XPATH, value='//*[@id="p_11647634"]/div/div[2]/div[3]').text #TODO find out how to make this work with coloured in stars
        print(rating)

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

    def scroll_to_more_books(self):
        scroll = self.scroll()
        time.sleep(1)
        scroll = self.scroll()
        time.sleep(1)
        scroll = self.scroll()
        time.sleep(1)
        show_more_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div[3]/button')
        show_more_button.click()
        time.sleep(2)
        scroll = self.scroll()
        time.sleep(1)

    def get_list_of_links(self):
        book_shelf = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div[2]')
        book_list = book_shelf.find_elements(by=By.XPATH, value='./div')
        list_of_links = []

        for book in book_list:
            a_tag = book.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            list_of_links.append(link)

        print (f'There are {len(list_of_links)} books on this page')
        print(list_of_links)

```

![](Screenshots/Milestone1.png) 

## Milestone 4

In this milestone I have used the Scraper() class from the previous milestone as a template to retrieve the text and image data from the page. I created a crawler to iterate through the URLs in my list_of_links and extract the data, storing them in a raw_data folder. Each book is saved in the folder as their unique ISBN number, and each folder contains a Json file with the extracted text data, and a jpeg image of the cover of the book. 