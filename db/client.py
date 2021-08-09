from pymongo import MongoClient
import yaml
import os

config_dir = os.path.dirname(__file__)[:-2] + "config.yaml"
with open(config_dir) as config:
    result = yaml.safe_load(config)
    HOST = result.get("host")
    PORT = result.get("port")
client = MongoClient(host=HOST, port=PORT)
