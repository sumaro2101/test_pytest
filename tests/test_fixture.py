import pytest
import json

@pytest.mark.fixture
def test_fixture_path(path_to_test):
    with path_to_test.open() as f:
        file_json = json.load(f)
        
    assert file_json[0]['id'] == 441945886
    
@pytest.mark.fixture
def test_init_fixture(init_json):
    assert init_json[1]['operationAmount']['amount'] == '70946.18'