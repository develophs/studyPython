# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["a", "b", "c", "d"]
    print(words)
    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    my_list = [1, 2, "str", True, False]
    print(my_list)
    my_list.append("True")
    my_list.append("False")
    print(my_list)
    for s in my_list:
        print(s)

    # List는 인덱스로 접근하고 값변경이 가능하다. 대괄호[]
    my_list[0] = 10
    print(my_list)

    # Tuple은 소괄호 (), 값변경이 불가능하다.
    my_tuple = (1, 2, 3, 4, 5)
    print(my_tuple)
    # my_tuple[0] = 10

    # Dictionary 키:벨류 형태, {} 중괄호를 사용한다.
    my_dictionary = {"키": 170, "몸무게": 70}
    print(my_dictionary['키'])
    print(my_dictionary['몸무게'])
    print(my_dictionary.get("키"))
    print(my_dictionary.get("몸무게"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
