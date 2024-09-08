import json
import yaml
import os
import toml
import configparser


def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def load_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def load_env():
    return {key: value for key, value in os.environ.items()}

def load_toml(file_path):
    with open(file_path, 'r') as f:
        return toml.load(f)

def load_ini(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return {section: dict(config[section]) for section in config.sections()}