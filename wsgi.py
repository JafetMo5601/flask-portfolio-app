import os

from config import DevConfig, ProdConfig
from src import create_api, parse_args

if (os.getenv('ENVIRONMENT', 'prod') == 'env'): 
    api = create_api(DevConfig)
else: 
    api = create_api(ProdConfig)

    
if __name__ == '__main__':
    api.run()
