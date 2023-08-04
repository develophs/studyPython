if __name__ == '__main__':
    # Slicing
    # x<=slice<y
    # 원본은 유지되고 새로운 문자열을 만든다.
    my_str = '김왼손의 왼손코딩'
    my_slice_str = my_str[:4]
    my_slice_str2 = my_str[5:9]
    print(my_slice_str)
    print(my_slice_str2)
    print(my_str[5:7])
    print(my_str[5:])

    #string.split() : default 문자열을 공백 단위로 잘라준다.
    my_name = '김왼손의 왼손코딩'
    print(my_name.split())
    print(my_name.split()[0])
    print(my_name.split()[1])
    fruit_str = '거봉 수박 포도 복숭아 망고 딸기 배 참외'
    print(fruit_str.split())
    korean = "가,나,다,라,마,바,사"
    print(korean.split())
    print(korean.split(","))

    #end : 출력되는 마지막 문자열을 지정할 수 있다.
    #end를 쓰면 엔터가 안된다.
    print(my_name, end=" 마지막 문자를 추가한다.\n")

    #escape : \n :엔터 \t: 탭
    print('미운코딩새끼들의 집단 지성들')
    print('미운코딩새끼들의\n집단 지성들')
    print('미운코딩새끼들의\t집단\n지성들')