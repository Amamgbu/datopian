import settings
from extract_data import extract_data

if __name__ == '__main__':
    #Enter an API key
    extract_data(settings.API_KEY,settings.FREQUENCY)