from flask import Flask
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Portfolio')
    parser.add_argument(
        '--enable-prod',
        action='store_true',
        default=False,
        help='Flag for production deployment. Warning: This will disable debugging mode.'
    )
    return parser.parse_args()



def create_api(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    # import blueprint and register them

    return app