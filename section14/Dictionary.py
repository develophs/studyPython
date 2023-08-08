if __name__ == '__main__':
    # Dictionary
    # {key1 : val1, key2 : val2}

    my_dict = {}
    print(my_dict)
    print(type(my_dict))

    #숫자0이 key이고 'a'가 값이다.
    my_dict[0] ='a'
    print(my_dict)

    #문자'b'가 key이고 2가 값이다.
    my_dict['b'] = 2
    print(my_dict)

    my_dict['학생1'] = '호박'
    print(my_dict)

    print(my_dict.get('학생1'))
    print(my_dict['학생1'])

    #key가 중복되면 이전 데이터는 삭제된다.
    my_dict['학생1'] = '고구마'
    print(my_dict)

    # 데이터 제거 dic dictionary[key]
    del my_dict[0]
    print(my_dict)
