import argparse
import os
import yaml
from src.process import Process

class Start():
    
    def __init__(self, config):

        name_yml = os.path.abspath(config)
        with open(name_yml, 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile,Loader=yaml.BaseLoader)

    def main(self):
        Process(self.cfg).process()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-cfg','--config',default='./config.yml')
    args = parser.parse_args()
    config = args.config

    Start(config).main()
