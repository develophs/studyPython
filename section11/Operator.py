if __name__ == '__main__':
    # 산술연산자, 대입연산자
    my_int = 10
    my_float = 2.0
    my_list = []

    my_int += 2
    print(my_int)

    my_float -= 0.1
    print(my_float)

    # 실수로 출력된다.
    my_int /= 2
    print(my_int)

    my_float %= 1.9
    print(my_float)

    # ** 제곱
    print("**", 3 ** 3)
    print("**", 2 ** 10)

    # // 몫 (정수)
    print("//", 3 // 3)
    print("//", 90 // 3)

    # % 나머지
    print("%", 3 % 3)
    print("%", 90 % 3)

    # 홀수 짝수 구하기
    numbers = range(1, 10)
    for num in numbers:
        print("짝수면 True {} = {}".format(num, num % 2 == 0))

    