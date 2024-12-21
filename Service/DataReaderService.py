import yaml
from redis import Redis

yml_file = "config.yml"
with open(yml_file, "r") as file:
    config = yaml.safe_load(file)

class DataReaderService:
    def __init__(self):
        self.host = config['redis']['host']
        self.port = config['redis']['port']

    def data_reader(self, key):
        r = Redis(host=self.host, port=self.port, decode_responses='True', db=0)
        return r.hgetall(key)