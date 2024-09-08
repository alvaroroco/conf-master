import configparser
import json

import toml
import yaml


def save_json(file_path, config):
    print(type(config))
    with open(file_path, "w") as f:
        json.dump(config, f, indent=4)


def save_yaml(file_path, config):
    with open(file_path, "w") as f:
        yaml.safe_dump(config, f, default_flow_style=False)


def save_toml(file_path, config):
    with open(file_path, "w") as f:
        toml.dump(config, f)


def save_ini(file_path, config):
    ini_config = configparser.ConfigParser()

    for section, section_data in config.items():
        if isinstance(section_data, list):
            for i, value in enumerate(section_data):
                ini_config[f"{section}_{i}"] = value
        else:
            ini_config[section] = section_data

    with open(file_path, "w") as f:
        ini_config.write(f)
