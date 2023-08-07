if __name__ == '__main__':
    # if 조건 :
    #\t명령1
    #\t명령2

    input_name = '김왼손'

    if input_name == '김왼손':
        print('만나서 반가워요', input_name)

    print("if 코드블럭 밖")
    
    # if : True일 경우 if문이 실행되고
    # else : False일 경우 elese문이 실행된다.
    
    # if
    # elif : if문이 False인 경우 해당 조건을 판단한다. > True : elif 블럭 실행
    #      : elif도 모두 False 경우 else문이 실행된다.
    # else

    input_s = input('이름 입력 : ')
    if input_s == '김왼손':
        print("당신이 김왼손이군요!")
    elif input_s == '호박':
        print("호박 호박")
    elif input_s == '고구마':
        print("고구마")
    else:
        print("누구")
    
    