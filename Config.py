import json


class Config:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.conf = json.load(file)

    def __call__(self, key):
        return self.conf.get(key)

    def __str__(self):
        return str(self.conf)

    def get_conf(self):
        return self.conf

    def return_args(self):
        return tuple(self.conf.values())


config = Config("config.json")
