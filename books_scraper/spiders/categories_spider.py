import scrapy
from books_scraper.items import Category

class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    
    start_urls = [
        'http://books.toscrape.com/index.html'
    ]
    
    def parse(self, response):
        selector = scrapy.Selector(response)
        
        for category_selector in selector.css('div.side_categories > ul > li > ul > li > a'):
            category = Category()
            category["name"] = category_selector.css('::text').get().strip()
            category["url"] = "http://books.toscrape.com/" + category_selector.attrib["href"].strip()
            yield category