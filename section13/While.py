if __name__ == '__main__':
    # 반복문 : for, while
    # 반복 횟수가 정해져있는 경우 for문
    # 반복 횟수를 잘 모를경우 while문

    # while 조건:
    #\t실행문1
    #\t실행문2
    
    #무한 루프 조심
    my_num = 1

    while my_num < 10:
        print(my_num, '은 10보다 작다')
        ## my_num++ 에러. ++문법은 존재하지 않는다.
        my_num += 1