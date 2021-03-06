# main.py
from botzibazor import Botzibazor
import logging
import os

token_bazibazor_prod = os.environ['TOKEN_PROD']

def main():

    logging.basicConfig(filename='botzibazor.log', level=logging.WARNING)
    logging.info('Started')

    botzibazor = Botzibazor(token_bazibazor_prod)
    botzibazor.start()

if __name__ == "__main__":
    main()