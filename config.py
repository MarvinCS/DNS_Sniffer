import json
import os


class Config:
    db_name = "dns.db"
    project_path = os.path.dirname(os.path.abspath(__file__))
    channel = None
    interface = None
    update_interval = None
    excluded_domains = []
    _log_window = None
    _scanning_thread = True

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
        if data["db_name"] is not None:
            Config.db_name = data["db_name"]
        if data["auto_update"] is not None:
            Config.update_interval = data["auto_update"]

    @staticmethod
    def chooseInterface():
        print('Available network-interfaces:')
        os.system('ifconfig -a | sed \'s/[ \t].*//;/^\(lo\|\)$/d\'')
        return input('\nWhich one do you want to use?\n')

    @staticmethod
    def save():
        data = {"db_name": Config.db_name, "channel": Config.channel, "auto_update": Config.update_interval,
                "interface": Config.interface, "excluded_domains": Config.excluded_domains}
        path_to_config = Config.project_path + "/config.json"
        with open(path_to_config, 'w') as outfile:
            json.dump(data, outfile)
