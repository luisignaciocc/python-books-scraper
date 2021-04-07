# Python Books Scraper

Scraper build with scrapy to get data from [here](https://books.toscrape.com/).

## Usage

You can run this project with or without Docker.

### With Docker

On the project root

```bash
docker-compose up
```

### Without Docker

Configure the respective database connection (MySQL) and enviroment on the config.yml file.

```bash
pip install -r requirements.txt
```

```bash
python3.6 start.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
