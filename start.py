import argparse
import os
import yaml
import datetime
import logging
# import mysql.connector
from src.process import Process

class Start():
    
    def __init__(self, config):

        name_yml = os.path.abspath(config)
        
        with open(name_yml, 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile,Loader=yaml.BaseLoader)
        
        logfile='./log/scraping-{:%Y_%m_%d_%H_%M}.log'.format(datetime.datetime.now())
        
        logging.basicConfig(
            level=logging.INFO,
            filename=logfile,
            datefmt='%Y-%m-%d %H:%M:%S',
            format='%(asctime)s %(levelname)-8s %(message)s')
        
        self.logger = logging.getLogger('scraper')
        
        """ try:
            self.conn = mysql.connector.connect(
                host=self.cfg['auth'][self.cfg['env']]['mysql-host'],
                user=self.cfg['auth'][self.cfg['env']]['mysql-user'],
                password=self.cfg['auth'][self.cfg['env']]['mysql-pass'],
                database=self.cfg['auth'][self.cfg['env']]['mysql-db']
            )
            self.cursor = self.conn.cursor(dictionary=True,buffered=True)
        except Exception as e:
            self.logger.error('ERROR CONECTING TO MySQL')
            self.logger.exception(e)
            quit() """

    def main(self):
        self.logger.info(f'PROCESS STARTED')
        Process(self.logger).process()
        self.logger.info(f'PROCESS FINISHED')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-cfg','--config',default='./config.yml')
    args = parser.parse_args()
    config = args.config

    Start(config).main()
