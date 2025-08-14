import pytest

from asynscan.utils.ports import parse_ports


def test_parse_ports_list_and_range():
    assert parse_ports("22,80,443") == [22, 80, 443]
    assert parse_ports("1-3") == [1, 2, 3]
    assert parse_ports("22,80,1000-1002") == [22, 80, 1000, 1001, 1002]


def test_parse_ports_invalid():
    with pytest.raises(ValueError):
        parse_ports("0")
    with pytest.raises(ValueError):
        parse_ports("70000")
    with pytest.raises(ValueError):
        parse_ports("10-5")
