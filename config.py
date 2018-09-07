import json
import os


class Config:

    def __init__(self):
        self.project_path = os.path.dirname(os.path.abspath(__file__))
        self.channel, self.update_interval = None, None

    def parse_config(self, path_to_config=None):
        if path_to_config is None:
            path_to_config = self.project_path + "/config.json"
        with open(path_to_config) as f:
            data = json.load(f)
        self.channel, self.update_interval = data["channel"], data["update_interval"]


config = Config()
config.parse_config()
