import os
import sys
import pytest
if sys.version_info >= (3, 3):
    from unittest.mock import MagicMock,patch
else:
    from mock import MagicMock,patch

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent+'/hw')

import task_2_mock_input
from test_task02_html import htmlcode,htmlcode2

@patch("task_2_mock_input.urllib.request.urlopen")
def test_positive_case(mock_urlopen):
    """Testing wrong case"""
    cm = MagicMock()
    cm.getcode.return_value = 200
    cm.read.return_value= htmlcode2
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm
    assert task_2_mock_input.count_dots_on_i(r'https://ya.ru/')==3892

@patch("task_2_mock_input.urllib.request.urlopen")
def test_negative_case(mock_urlopen):
    """Testing wrong case"""
    cm = MagicMock()
    cm.getcode.return_value = 200
    cm.read.return_value= htmlcode
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm
    assert not task_2_mock_input.count_dots_on_i(r'https://ya.ru/')==0

