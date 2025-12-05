import pytest
import day2
import common

def test_get_ranges():

    lines = common.read_input("input_test")
    assert day2.get_ranges(lines) == ["11-22", "95-115", "998-1012", "1188511880-1188511890","222220-222224",
                                "1698522-1698528", "446443-446449", "38593856-38593862", "565653-565659",
                                 "824824821-824824827","2121212118-2121212124"]

def test_idrange():
    idrange = day2.IdRange("11-22")
    assert idrange.to_string() == "11-22"
    assert idrange.get_invalids1() == [11, 22]
    idrange = day2.IdRange("95-115")
    assert idrange.get_invalids1() == [99]
    assert idrange.get_invalids2() == [99, 111]
    idrange = day2.IdRange("998-1012")
    assert idrange.get_invalids1() == [1010]
    assert idrange.get_invalids2() == [999, 1010]
    idrange = day2.IdRange("38593856-38593862")
    assert idrange.get_invalids1() == [38593859]
    assert idrange.get_invalids2() == [38593859]
    idrange = day2.IdRange("2121212118-2121212124")
    assert idrange.get_invalids1() == []
    assert idrange.get_invalids2() == [2121212121]

def test_addup_invalids():
    lines = common.read_input("input_test")
    assert day2.addup_invalids1(lines) == 1227775554
    assert day2.addup_invalids2(lines) == 4174379265

    lines = common.read_input("input")
    assert day2.addup_invalids1(lines) == 29940924880
    assert day2.addup_invalids2(lines) == 48631958998