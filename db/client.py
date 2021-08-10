from pymongo import MongoClient
import yaml

with open('config.yaml', 'r') as config:

    result = yaml.safe_load(config)
    HOST = result.get("host")
    PORT = result.get("port")

client = MongoClient(host=HOST, port=PORT)
