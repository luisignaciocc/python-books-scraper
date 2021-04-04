import sys
import subprocess
import json
import os

class ScrapyAgent():

    def get_crawler_categories_data(self):
            which_python = sys.executable
            env_path = which_python.rsplit('/', 1)[0] + '/'
            scrapy_path = env_path + 'scrapy'

            json_file_path = "scrapers_output/%s.json" % "categories"

            subprocess.check_output([scrapy_path, 'crawl', 'categories', '-O', json_file_path])
            with open(json_file_path) as json_file:

                data = json.load(json_file)

                return data

    def get_crawler_books_data(self, category):
            which_python = sys.executable
            env_path = which_python.rsplit('/', 1)[0] + '/'
            scrapy_path = env_path + 'scrapy'

            json_file_path = "scrapers_output/books_%s.json" % category.name.lower().replace(' ', '_')

            subprocess.check_output([scrapy_path, 'crawl', '-a', f'start_url={category.url}', 'books', '-O', json_file_path])
            with open(json_file_path) as json_file:

                data = json.load(json_file)

                return data
