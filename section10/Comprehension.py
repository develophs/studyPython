if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = []

    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)

    print(odd_numbers)

    # Comprehension
    # 복잡한 로직을 한줄로 표현할 수 있다.
    # 정말 많이 사용된다.
    odd_numbers2 = [number for number in numbers if number % 2 == 1]
    print(odd_numbers2)

    even_number = [number for number in numbers if number % 2 == 0]
    print(even_number)