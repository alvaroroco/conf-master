import json

import toml
import yaml


def test_load_from_json(conf_master, config_data, test_files):
    test_json, _, _ = test_files
    with open(test_json, "w") as f:
        json.dump(config_data, f)

    conf_master.load_from_json(test_json)
    assert conf_master.get("database.host") == "localhost"
    assert conf_master.get("database.port") == 5432


def test_load_from_yaml(conf_master, config_data, test_files):
    _, test_yaml, _ = test_files
    with open(test_yaml, "w") as f:
        yaml.safe_dump(config_data, f)

    conf_master.load_from_yaml(test_yaml)
    assert conf_master.get("database.host") == "localhost"
    assert conf_master.get("database.port") == 5432


def test_load_from_toml(conf_master, config_data, test_files):
    _, _, test_toml = test_files
    with open(test_toml, "w") as f:
        toml.dump(config_data, f)

    conf_master.load_from_toml(test_toml)
    assert conf_master.get("database.host") == "localhost"
    assert conf_master.get("database.port") == 5432


# TODO: Add more tests (.env)
