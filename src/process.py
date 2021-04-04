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

        self.logger.info('--* ALEMBIC MIGRATION *--')
        alembicArgs = ['--raiseerr', '-x', f'dbUrl={SQLALCHEMY_DATABASE_URI}', 'upgrade', 'head']
        alembic.config.main(argv=alembicArgs)
        self.logger.info('--* ALEMBIC MIGRATION *--')

        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(self.engine)
        self.session = Session()


    def process(self):
        self.logger.info(' -----------------')
        self.logger.info('| PROCESS STARTED |')
        self.logger.info(' -----------------')

        categories_data = self.get_crawler_categories_data()
        for item in categories_data:
            
            category = self.session.query(Category).filter(Category.name.like(item['name'])).one_or_none()
            
            if category is None:
                category = Category(
                    name = item['name'],
                    url = item['url']
                )
                self.session.add(category)
                try:
                    self.session.commit()
                except IntegrityError:
                    self.logger.error(f'{category.name} already inserted')
                    self.session.rollback()
                else:
                    self.logger.info(f'{category.name} inserted')
                    category_id = category.id
                    category_name = category.name
            else:
                self.logger.error(f'{category.name} already inserted')
                category_id = category.id
                category_name = category.name

            print(category_id)
            print(category_name)
            books_data = self.get_crawler_books_data(category)

        self.logger.info(' ------------------')
        self.logger.info('| PROCESS FINISHED |')
        self.logger.info(' ------------------')


if __name__ == '__main__':
    Process().process()
