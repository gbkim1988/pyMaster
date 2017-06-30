# case 1 : key 가 존재하지 않을 때, 오류 처리
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
import pytest

def test_there_is_no_key_in_dictionary():
    dictionary_obj = dict()
    # setdefault 메서드를 통해서, 키가 존재하지 않을 시에 생성할 키와 default value 를 지정할 수 있다.
    dictionary_obj.setdefault('test', str('you fucked'))

    dictionary_obj['none'] = 'none'
    assert dictionary_obj.get('merong') == str('you fucked')
    print(dictionary_obj.get('test'))
    try:
        dictionary_obj['non']
    except KeyError as error:
        print("KeyError {0}".format(error))
    # key 에 대한 값을 적절히 가져올 수 있는 방법 1
    # get 은 키가 없을 경우, None 을 출력한다.
    assert dictionary_obj.get('none') == "none"
    assert dictionary_obj.get('nokey') == None
    # 만약 키가 존재하지 않을 경우 default 값으로 정수 11을 출력
    assert dictionary_obj.get('nokey_again', int(11)) == 11
    assert dictionary_obj.get('test') == str('you fucked')
    # 업데이트는 키워드 파라미터로 키에 대한 수정이 가능하다.
    dictionary_obj.update(none="updated")

    assert dictionary_obj.get('none') == 'updated'

test_there_is_no_key_in_dictionary()