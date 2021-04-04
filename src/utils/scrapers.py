import sys
import subprocess
import json
import os

class ScrapyAgent():

    def get_crawler_data(self, scraper_name):
            which_python = sys.executable
            env_path = which_python.rsplit('/', 1)[0] + '/'
            scrapy_path = env_path + 'scrapy'

            json_file_path = "scrapers_output/%s.json" % scraper_name

            subprocess.check_output([scrapy_path, 'crawl', scraper_name, '-O', json_file_path])
            with open(json_file_path) as json_file:

                data = json.load(json_file)

                return data
