if __name__ == '__main__':
    # 문자열 연산자
    # 문자열에서 + 연산자는 문자열을 붙인다.
    my_str = "안녕하세요"
    my_str2 = " 반갑습니다."
    print(my_str + my_str2)

    # 문자열 + 숫자 >> 안된다.
    my_num = 10
    # print(my_str + my_num)

    # 문자열 * 숫자 > 해당 문자열을 숫자만큼 반복한다.
    print(my_str * 3)
    print(my_str2 * 2)


    # 1을 100번 출력한다.
    def cls():
        print('1\n' * 100)


    cls()
