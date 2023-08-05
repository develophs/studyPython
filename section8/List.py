if __name__ == '__main__':
    # List 여러가지 데이터 타입 및 데이터를 가진다.
    # 데이터를 변경할 수 있으며
    # 중복을 허용하고 순서를 보장한다.
    my_list = [1, 2, True, False, "가", "나", "다"]
    print(my_list)
    my_empty_list = []
    print(type(my_empty_list))

    # List.append()
    print('empty', my_empty_list)
    my_empty_list.append("가")
    my_empty_list.append("나")
    my_empty_list.append("다")
    print('appendList', my_empty_list)
    my_empty_list.append(1)
    print('appendList2', my_empty_list)
    my_empty_list.append([2, 3, 4, 5, 6, 7, 8, 9, 10])
    print('appendList3', my_empty_list)
    print(my_empty_list[4])
    print(my_empty_list[4][0])
    print(my_empty_list[4][1])
    print(my_empty_list[4][2])

    # del() : 해당 인덱스의 데이터를 제거한다.
    del(my_empty_list[4])
    print(my_empty_list)

    # List.sort(): 오름차순, List.reverse(): 내림차순
    my_sort_list = [2, 3, 5, 6, 7, 8, 9, 1, 4]
    my_sort_list.sort()
    print('sort', my_sort_list)
    my_sort_list2 = ['나', '다', '라', '가', '타', '자']
    my_sort_list2.sort()
    print(my_sort_list2)
    my_sort_list.reverse()
    print('reverse', my_sort_list)

    # List.count()
    number_list = [1, 2, 3, 1, 2, 3, 1]
    count = number_list.count(1)
    count2 = number_list.count(4)
    print(count)
    print(count2)

    #len()
    length = len(number_list)
    len(number_list)
