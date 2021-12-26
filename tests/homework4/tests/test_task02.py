import sys

if sys.version_info >= (3, 3):
    from unittest.mock import MagicMock, patch
else:
    from mock import MagicMock, patch

from homework_04.hw.task_2_mock_input import count_dots_on_i

from tests.homework4.tests.test_task02_html import htmlcode, htmlcode2


@patch("urllib.request.urlopen")
def test_positive_case(mock_urlopen):
    """Testing wrong case"""
    cm = MagicMock()
    cm.getcode.return_value = 200
    cm.read.return_value = htmlcode2
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm
    assert count_dots_on_i(r'https://ya.ru/') == 3892


@patch("urllib.request.urlopen")
def test_negative_case(mock_urlopen):
    """Testing wrong case"""
    cm = MagicMock()
    cm.getcode.return_value = 200
    cm.read.return_value = htmlcode
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm
    assert not count_dots_on_i(r'https://ya.ru/') == 0
