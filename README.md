# Python Books Scraper

Scraper build to get data from [here](https://books.toscrape.com/).

## Build with

* [Scrapy](https://scrapy.org)
* [SQLAlchemy](https://www.sqlalchemy.org)
* [Alembic](https://alembic.sqlalchemy.org/en/latest)

## Usage

### With Docker Compose

On the project root

```bash
docker-compose up
```

### Without Docker

You'll need to create and activate a new python3.6 virtual enviroment and configure the respective MySQL database connection on the config.yml file.

```bash
pip install -r requirements.txt
```

```bash
python3.6 start.py
```

#### After execution, the data will be parsed in the database. There is a table for books and a table for categories. The exposed port of the database in the Docker container is 3336 (MySQL)

## License
[MIT](https://choosealicense.com/licenses/mit/)
