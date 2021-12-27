import pytest
import os.path
import json
from homework_10.hw.parser_sp500 import Parser_sp500

path_to_file1 = os.path.join(os.path.dirname(__file__), 'top_highest_price.json')
path_to_file2 = os.path.join(os.path.dirname(__file__), 'top_lowest_pe.json')
path_to_file3 = os.path.join(os.path.dirname(__file__), 'top_with_max_growth.json')
path_to_file4 = os.path.join(os.path.dirname(__file__), 'top_highest_potential_profit.json')

@pytest.fixture
def prepare_data():
    parser = Parser_sp500()
    parser.parse()
    with open(path_to_file1, 'w') as file:
        json.dump(parser.top_highest_price, file)
    with open(path_to_file2, 'w') as file:
        json.dump(parser.top_lowest_pe, file)
    with open(path_to_file3, 'w') as file:
        json.dump(parser.top_with_max_growth, file)
    with open(path_to_file4, 'w') as file:
        json.dump(parser.top_highest_potential_profit, file)


def test_positive_case(prepare_data):
    """Testing correct cases"""
    with open(path_to_file1, 'r') as json_file:
        data = json.load(json_file)
        assert len(data['data']) == 10
    with open(path_to_file3, 'r') as json_file:
        data = json.load(json_file)
        assert len(data['data']) == 10

def test_negative_case(prepare_data):
    """Testing wrong cases"""
    with open(path_to_file2, 'r') as json_file:
        data = json.load(json_file)
        assert len(data['data']) != 0
    with open(path_to_file4, 'r') as json_file:
        data = json.load(json_file)
        assert len(data['data']) != 0
