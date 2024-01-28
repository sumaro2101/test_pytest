import json
import pytest
from utils.functions import open_json, sorting_by_executed, sorting_by_string, output_trans

@pytest.mark.utils
class TestsUtils:
    def test_open_json(self, path_to_test, init_json):
        with open(path_to_test, encoding='utf-8') as f:
            test = json.load(f)
        assert test == init_json


    def test_sorting_by_executed(self, init_json):
        """Если подаётся ключ 'state' со значением 'CANCELED',
        тест операцию не засчитывает"""
        sort = len([item["state"] for item in init_json if item["state"] == "EXECUTED"])
        assert sort == 2


    def test_sorting_by_string(self, init_json):
        """Проверка на правильную сортировку с верной длиной"""
        file = sorting_by_string(init_json)
        assert file[0]['date'] > file[1]['date'] > file[2]['date']


    def test_output_trans(self, init_json):
        """Проверка на правильную реформацию входящих данных"""
        input_ = [init_json[0]]
        assert output_trans(input_) == ['26.08.2019 Перевод организации\n'
                                        'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                        '31957.58 руб.\n']
