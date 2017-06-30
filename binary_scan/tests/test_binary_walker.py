import pytest
import binary_walker
import mmap
from builtins import bytearray

def test_binary_string_accuracy():
    #binary_walker.file_to_strings()
    #실행 바이너리를 문자열화하면 오프셋 0~1 의 문자열은 MZ 일것이다.
    assert binary_walker.file_to_strings('C:\\Windows\\System32\\cmd.exe')[:2] == b'MZ'
