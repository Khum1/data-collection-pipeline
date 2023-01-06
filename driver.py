from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chromeOptions = Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--window-size=1920,1080")
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-setuid-sandbox")
chromeOptions.add_argument("--disable-gpu")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
chromeOptions.add_argument(f'user-agent={user_agent}')

class Driver:
    def __init__(self):
        '''
        Initiallises the driver for use.

        Parameters
        ----------
        None
        '''
        
    def get_driver():
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        return driver