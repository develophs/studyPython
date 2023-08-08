if __name__ == '__main__':
    # 함수 : 반복되는 코드를 하나의 함수로 만들어 반복적으로 사용가능하다.
    # 내장함수 : 파이썬 자체의 함수
    # 모듈의 함수 : import 후 사용할 수 있는 함수
    # 사용자 정의 함수 : 사용자가 직접 만들어 사용하는 함수

    # def(define) 함수이름(args...):
    #   실행할 명령1
    #   실행할 명령2
    #   return 결과

    # 값1개 리턴
    def add(num1, num2):
        return num1 + num2


    print(add(100, 30))


    # 값을 여러개 리턴해야하는경우
    # return value1, value2, value3...

    def add_mul(num1, num2):
        return num1 + num2, num1 * num2

    #Tuple로 반환된다.
    my_numbers = add_mul(1, 2)
    print(my_numbers[0])
    print(my_numbers[1])

    #언패킹
    my_add, my_mul = add_mul(2,2)
    print(my_add)
    print(my_mul)
