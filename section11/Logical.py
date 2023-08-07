if __name__ == '__main__':
    ## and >> && 없다.
    print(True and False)

    ## or >> || 없다.
    print(True or False)

    ## not >> ! 없다.
    print(not True)
    print(not False)

    height = 120
    age = 8

    print(height > 140 and age > 10)
    print(height < 140 or age > 10)
    print(not height > 140 and not age > 10)
    print(not height > 140 or age > 10)

    # Membership
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('1 is in my_list', 1 in my_list)
    print('11 is in my_list', 11 in my_list)

    print('1 is not in my_list', 1 not in my_list)
    print('11 is not in my_list', 11 not in my_list)

    my_list.append(11)
    print('11 is in my_list', 11 in my_list)