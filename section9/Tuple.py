if __name__ == '__main__':
    # Tuple () 소괄호로 정의한다.
    # 소괄호가 없어도 지정할 수 있다.
    # 순서를 보장하며 중복값을 허용한다
    # 하지만, 값변경이 불가능하다. immutable

    my_tuple = (1, 2, 3, 4, 5)
    print(my_tuple)
    # my_tuple.append(1) : 에러
    # my_tuple[4]=6 : 에러
    print(type(my_tuple))

    my_tuple2 = 1, 2, 3
    print(my_tuple2)
    print(type(my_tuple2))

    # packing, unpacking
    num1, num2, num3, num4, num5 = my_tuple
    print(num1, num2, num3, num4, num5)
    num1, num2 = num2, num1
    print('num1', num1)
    print('num2', num2)
