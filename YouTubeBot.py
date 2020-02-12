from selenium import webdriver
from time import sleep

class YouTubeBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def search(self):
        self.driver.get('https://youtube.com')

        sleep(1)
        
        yt_search = self.driver.find_element_by_xpath('//*[@id="search"]')
        yt_search.send_keys('Hitesh Choudhary')

        yt_btn = self.driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
        yt_btn.click()

def main():
    bot = YouTubeBot()
    bot.search()

if __name__ == "__main__":
    main()
