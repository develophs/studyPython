if __name__ == "__main__":
    # 이중 for문
    # for i in range(1, 10):
    #     for n in range(1, 10):
    #         print(i, "*", n, "=", i * n)

    #format을 이용한 방법
    #format은 문자열에 사용하는 메소드이다.
    for i in range(1, 10):
        for n in range(1, 10): #탭1번
            print("{} * {} = {}".format(i, n, i * n))#탭2번
        print("{}단 출력 종료".format(i))
    print("구구단 출력 종료")
