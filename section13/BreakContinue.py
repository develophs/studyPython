if __name__ == '__main__':
    # continue : continue를 만나면 continue아래 코드들은 실행되지 않는다.
    # break : break를 만나면 해당 반복문은 종료된다.

    count = 0

    while count < 20:
        count += 1
        if count <= 9:
            continue
        print(count)
        if count == 10:
            break
