import json
import os


class Config:
    db_name = "dns.db"
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
        if data["db_name"] is not None:
            Config.db_name = data["db_name"]

    @staticmethod
    def chooseInterface():
        print('Available network-interfaces:')
        os.system('ifconfig -a | sed \'s/[ \t].*//;/^\(lo\|\)$/d\'')
        return input('\nWhich one do you want to use?\n')

    @staticmethod
    def save():
        data = {"db_name": Config.db_name, "update_interval": Config.update_interval, "channel": Config.channel,
                "interface": Config.interface, "excluded_domains": Config.excluded_domains}
        path_to_config = Config.project_path + "/config.json"
        with open(path_to_config, 'w') as outfile:
            json.dump(data, outfile)
