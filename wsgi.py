import os

from config import DevConfig, ProdConfig
from src import create_api, parse_args

def main(enable_prod: bool):    
    if enable_prod: 
        host = '0.0.0.0'
#         port = 5900
        api = create_api(ProdConfig)
    else: 
        host = '127.0.0.1'
#         port = 3000
        api = create_api(DevConfig)
        
    api.run(host=host)
        

if __name__ == '__main__':
    args = parse_args()
    main(args.enable_prod) # 
