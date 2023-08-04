if __name__ == '__main__' :
    #문자열은 "" 더블쿼테이션, ''싱글쿼테이션 둘다 적용이 가능하다.
    my_string = "str"
    print(type(my_string))
    my_string2 = 'str2'
    print(type(my_string2))

    #""", '''쿼테이션 3개, 여러줄로 문자열 선언이 가능하다.
    my_strings = """
    김
    이
    박
    최
    """
    print(my_strings)