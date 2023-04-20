import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from xvfbwrapper import Xvfb


class AvitoParse:

    def __init__(self, url: str, items: list, max_price: int = 100000, count: int = 100, version_main: int = 112):
        self.max_price = max_price
        self.url = url
        self.items = items
        self.count = count
        self.version_main = version_main
        self.data = {}
        self.display = None

    def __set_up(self):
        self.display = Xvfb()
        self.display.start()
        self.driver = uc.Chrome(version_main=self.version_main)
        print('Starting Chrome')

    def __close_driver(self):

        self.driver.quit()
        self.display.stop()
        print('Closing Chrome')

    def __get_url(self):
        self.driver.get(self.url)

    def __parse_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_element(By.CSS_SELECTOR, "[class*='item-description']").text
            url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute("href")
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute("content")
            post_data = {
                'name': name,
                'description': description,
                'url': url,
                'price': price
            }
            if (any([item.lower() in name.lower() for item in self.items]) or any(
                    [item.lower() in description.lower() for item in self.items])) and int(price) <= self.max_price:
                self.data[url.split('_')[-1]] = post_data

        print(self.data)

    def check_update(self):
        fresh_posts = dict()
        with open("items.json", encoding="utf-8") as file:
            post_list = json.load(file)

        self.__set_up()
        self.__get_url()
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute("href")
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_element(By.CSS_SELECTOR, "[class*='item-description']").text
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute("content")
            post_data = {
                'name': name,
                'description': description,
                'url': url,
                'price': price
            }
            if (any([item.lower() in name.lower() for item in self.items]) or any(
                    [item.lower() in description.lower() for item in self.items])) and int(price) <= self.max_price:
                if url.split('_')[-1] not in post_list:
                    fresh_posts[url.split('_')[-1]] = post_data
                self.data[url.split('_')[-1]] = post_data
        self.__save_data()
        self.__close_driver()
        return fresh_posts

    def __save_data(self):
        with open("items.json", 'w', encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def parse(self):
        self.__set_up()
        self.__get_url()
        self.__parse_page()
        self.__save_data()
        self.__close_driver()
