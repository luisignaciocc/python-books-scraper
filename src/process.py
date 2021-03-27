from src.utils.scrapers import ScrapyAgent

class Process(ScrapyAgent):
    
    def __init__(self, logger):
        super()
        self.logger = logger

    def process(self):
        categories_data = self.get_crawler_data('categories')
        for item in categories_data:
            print(item)

if __name__ == '__main__':
    Process().process()
