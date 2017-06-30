import pytest
from directory_walker import search_directory, get_file_list


def test_search_directory_method():
    dict_dir = search_directory("D:\\IR-20170626-001\\artifact\\", ".*\.exe$")
    total_log = 0
    for i in dict_dir:
        total_log += len(dict_dir[i])
        if len(dict_dir[i]):
            assert open(dict_dir[i][0],'rb').readline()[0:2] == b'MZ'
    assert total_log == 420

def test_get_file_list_method():
    assert len(get_file_list("D:\\IR-20170626-001\\artifact\\", ".*\.txt$")) == 13
    assert open(get_file_list("D:\\IR-20170626-001\\artifact\\", ".*\.txt$")[0], 'rb').fileno()  < 0

def test_get_file_binary_file_list_method():
    # get list
    # regex pattern, test for virus total scan (\S+(?:png|dll|exe|docx|pdf|sys|scr|lnk))
    files = search_directory("D:\\IR-20170626-001\\artifact\\go_darie", r"(\S+(?:png|dll|exe|docx|pdf|sys|scr|lnk))")
    total_log = 0
    for i in files:
        total_log += len(files[i])
        for fname in files[i]:
            print(fname)
    assert len(total_log) > 10

test_get_file_binary_file_list_method()