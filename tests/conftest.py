import pytest
from conf_master import ConfMaster
from fixtures.fixture_data import config_data, schema  # noqa: F401


@pytest.fixture
def conf_master():
    return ConfMaster()


@pytest.fixture
def test_files(tmp_path):
    test_json = tmp_path / "test_config.json"
    test_yaml = tmp_path / "test_config.yaml"
    test_toml = tmp_path / "test_config.toml"

    return test_json, test_yaml, test_toml
