if __name__ == "__main__":
    # For문
    # for 변수 in 컨테이너:
    # 공백4번(탭) 후 원하는 로직
    # 파이썬은 들여쓰기가 필수이다. 공백4개 코드블럭을 구분한다.
    my_list = [1, 2, 3, 4, 5]
    for num in my_list:
        print(num)  # 공백이 4개존재해야 for문안(코드블럭)에 존재하는것이다.
    print("여기는 반복되어서는 안된다.")

    # 단순 문자열도 for문이 가능하다.
    for string in "김왼손의왼손코딩":
        print(string)

    # range()
    # 반복문의 횟수를 지정할 수 있다.
    print(type(range(3)))
    for i in range(0, 100):
        print(i)

    for i in range(5, 10):
        print(i)

    # 숫자를 하나만 넣은경우 0부터 range까지.
    for i in range(10):
        print(i)
