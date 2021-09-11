import os

from config import DevConfig, ProdConfig
from src import create_api, parse_args

if (os.environ['ENVIRONMENT'] == 'env'): 
    api = create_api(DevConfig)
else: 
    api = create_api(ProdConfig)

    
if __name__ == '__main__':
    api.run()
