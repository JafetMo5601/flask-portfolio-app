import os

from config import DevConfig, ProdConfig
from src import create_api

if (os.getenv('ENVIRONMENT', 'prod') == 'dev'): 
    api = create_api(DevConfig)
    host = '127.0.0.1'
else: 
    api = create_api(ProdConfig)
    host = '0.0.0.0'

    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    api.run(host=host, port=port)
