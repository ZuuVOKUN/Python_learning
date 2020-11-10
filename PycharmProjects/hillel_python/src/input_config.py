import json
import argparse


def parse_args():

    parser = argparse.ArgumentParser(description='JSON path analysis')

    parser.add_argument('--path',
                        type=str,
                        required=True,
                        help='Path to specification *.json file')

    return parser.parse_args()


args = parse_args()
print(args.path)

path_config = args.path
configs = open(path_config)

config = json.loads(configs.read())

company = config['company']
model = config['model']
color = config['color']
speed_limit = config['speed_limit']

print(company, model, color, speed_limit)