import random

# import random : random 모듈을 가져온다.

if __name__ == '__main__':
    # Module : 이미 구현되어있는 코드 모음, 함수 모음
    # import 후 사용해야한다.

    # random.choice : 해당 데이터에서 랜덤으로 뽑아온다.
    korean = ['가', '나', '다', '라', '마', '바', '사']
    print(random.choice(korean))
    print(random.choice(korean))
    print(random.choice(korean))
    print(random.choice(korean))
    print(random.choice(korean))
    print(random.choice(korean))
    print(random.choice(korean))
    print(random.choice(korean))

    # random.sample : 해당 데이터에서 갯수만큼 가져온다., 중복해서 출력X
    print(random.sample(korean, 4))
    print(random.sample(range(1, 45), 6))

    # random.randint() : 해당 범위의 정수의 값을 가져온다. 1개만 출력
    print(random.randint(8, 10))
    print(random.randint(1, 46))
