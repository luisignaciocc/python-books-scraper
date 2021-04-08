# Python Books Scraper

Scraper build with scrapy to get data from [here](https://books.toscrape.com/).

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

## License
[MIT](https://choosealicense.com/licenses/mit/)
