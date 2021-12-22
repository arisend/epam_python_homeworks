import os.path
import json
from homework_10.hw.parser_sp500 import Parser_sp500

path_to_file1 = os.path.join(os.path.dirname(__file__), 'top_highest_price.json')
path_to_file2 = os.path.join(os.path.dirname(__file__), 'top_lowest_pe.json')


parser = Parser_sp500()
with open('top_highest_price.json', 'w') as file:
    json.dump(parser.top_highest_price, file)
with open('top_lowest_pe.json', 'w') as file:
    json.dump(parser.top_lowest_pe, file)
with open('top_with_max_growth.json', 'w') as file:
    json.dump(parser.top_with_max_growth, file)
with open('top_highest_potential_profit.json', 'w') as file:
    json.dump(parser.top_highest_potential_profit, file)


def test_positive_case():
    """Testing correct cases"""
    with open(path_to_file1, 'r') as json_file:
        data = json.load(json_file)
        assert len(data['data']) == 10


def test_negative_case():
    """Testing wrong cases"""
    with open(path_to_file2, 'r') as json_file:
        data = json.load(json_file)
        assert len(data['data']) != 0
