if __name__ == '__main__':
    # 메소드 : 해당 데이터 타입만 사용할 수 있는 함수

    my_dict = {'1': '고구마', '2': '호박', '3': '감자'}

    # dictionary.values() : dictionary에서 값만 가져온다.
    print(my_dict.values())

    # dictionary.keys() : dictionary에서 key만 가져온다.
    print(my_dict.keys())

    for vegi in my_dict.values():
        print(vegi)

    for key in my_dict.keys():
        print(key)

    # dictionary.items() : 키, 벨류 모두 다 가져온다.
    # 키값은 ,를 기준으로 앞에 벨류값은 ,를 기준으로 뒤에위치한다.
    for key, val in my_dict.items():
        print(key, val)
