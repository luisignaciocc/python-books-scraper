import scrapy
from books_scraper.items import Book


class BooksSpider(scrapy.Spider):
    name = "books"
    
    def __init__(self, *args, **kwargs): 
        super(BooksSpider, self).__init__(*args, **kwargs) 
        self.start_urls = [kwargs.get('start_url')]
        self.base_url = 'http://books.toscrape.com/'

    def parse(self, response):
        selector = scrapy.Selector(response)
        for books_selector in selector.css('ol.row > li'):
            book_details_url = self.base_url + 'catalogue/' + books_selector.css('article > h3 > a').attrib["href"].strip().split("../")[3]
            yield scrapy.Request(book_details_url, callback = self.parse_book_contents, cb_kwargs=dict(main_url=book_details_url))
        
        try:
            next_page_herf = selector.css('li.next > a').attrib["href"].strip()
        except KeyError:
            print('Last page...')
        else:
            next_page_url = self.start_urls[0].rsplit('/', 1)[0] + '/' + next_page_herf
            yield scrapy.Request(next_page_url, callback = self.parse)

    def parse_book_contents(self, response, main_url):
        selector = scrapy.Selector(response)
        book = Book()
        book["name"] = selector.css('div.col-sm-6.product_main > h1::text').get().strip()
        book["price"] = selector.css('div.col-sm-6.product_main > p.price_color::text').get().strip().replace('£', '')
        book["url"] = main_url
        book["image_url"] = self.base_url + selector.css('#product_gallery > div > div > div > img').attrib["src"].split("../")[2]
        book["description"] = selector.css('#content_inner > article > p::text').get().replace('...more', '').strip()
        yield book