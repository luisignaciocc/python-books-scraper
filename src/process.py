import datetime
import logging
import alembic.config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.utils.scrapers import ScrapyAgent
from src.models.categories_model import Category

class Process(ScrapyAgent):

    def __init__(self, cfg):
        super()
        
        logfile='./log/scraping-{:%Y_%m_%d_%H_%M}.log'.format(datetime.datetime.now())
        logging.basicConfig(
            level=logging.INFO,
            filename=logfile,
            datefmt='%Y-%m-%d %H:%M:%S',
            format='%(asctime)s %(levelname)-8s %(message)s')
        self.logger = logging.getLogger('scraper')
        
        SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(
            cfg['auth'][cfg['env']]['mysql-user'],
            cfg['auth'][cfg['env']]['mysql-pass'],
            cfg['auth'][cfg['env']]['mysql-host'],
            cfg['auth'][cfg['env']]['mysql-port'],
            cfg['auth'][cfg['env']]['mysql-db'])

        alembicArgs = ['--raiseerr', '-x', f'dbUrl={SQLALCHEMY_DATABASE_URI}', 'upgrade', 'head']
        alembic.config.main(argv=alembicArgs)

        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(self.engine)
        self.session = Session()


    def process(self):
        categories_data = self.get_crawler_data('categories')
        for item in categories_data:
            category = Category(
                name = item['name'],
                url = item['url']
            )
            self.session.add(category)
            try:
                self.session.commit()
            except IntegrityError:
                self.logger.error(f'{category} already inserted')
                self.session.rollback()
            else:
                self.logger.info(f'{category} inserted')


if __name__ == '__main__':
    Process().process()
