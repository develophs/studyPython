if __name__ == '__main__' :
    # %d:정수 %s:문자 %f:실수
    my_str = 'My anme is %s' % 'BaeHanseong'
    print(my_str)
    my_height = 'My height is %d' % 173
    print(my_height)
    my_weight = 'My weight is %f' % 68.0
    print(my_weight)
    my_strs = '여러개 넣기 %s %s %s' % ('가','나','다')
    print(my_strs)

    #'{}'.format(), 자료형에 제한이없다. 파이썬스러운 문법
    my_str2 = 'My name is {}'.format('Baehanseong')
    print(my_str2)

    my_height2 = 'My height is {}'.format(173)
    print(my_height2)

    my_weight2 = 'My weight is {}'.format(68.0)
    print(my_weight2)

    my_strs2 = '여러개 넣기 {} {} {}'.format('가','나','다')
    print(my_strs2)
    
    my_str3 = '여러개 넣기 인덱스 접근 {1} {0} {2}'.format('나','가','다')
    print(my_str3)