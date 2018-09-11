import json
import os


class Config:
    update_interval = None
    project_path = os.path.dirname(os.path.abspath(__file__))
    channel = None
    interface = None
    excluded_domains = []

    @staticmethod
    def parse_config(path_to_config=None):
        if path_to_config is None:
            path_to_config = Config.project_path + "/config.json"
        with open(path_to_config) as f:
            data = json.load(f)
        Config.channel = data["channel"]
        if data["interface"] is not None:
            Config.interface = data["interface"]
        if data["excluded_domains"] is not None:
            Config.excluded_domains = data["excluded_domains"]
        Config.update_interval = data["update_interval"]

    @staticmethod
    def chooseInterface():
        print('Available network-interfaces:')
        os.system('ifconfig -a | sed \'s/[ \t].*//;/^\(lo\|\)$/d\'')
        return input('\nWhich one do you want to use?\n')
