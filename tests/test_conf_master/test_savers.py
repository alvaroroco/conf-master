import json

import pytest
from conf_master.exceptions import ConfigSaveError


def test_save_to_json(conf_master, config_data, test_files):
    test_json, _, _ = test_files
    conf_master.config = config_data
    conf_master.save_to_json(test_json)

    with open(test_json, "r") as f:
        loaded_config = json.load(f)

    assert loaded_config == config_data


def test_save_json_error(conf_master, config_data):
    conf_master.config = config_data

    with pytest.raises(ConfigSaveError):
        conf_master.save_to_json("/invalid/path/test_config.json")
