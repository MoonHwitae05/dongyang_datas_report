def super_add(*args):
    # args는 이제 (1, 2, 3, 4, 5) 라는 거대한 하나의 튜플 주머니가 되었습니다!
    total = 0
    for num in args:  # 주머니 안의 숫자를 for문으로 하나씩 꺼내 씁니다.
        total += num
    return total

print(super_add(10, 20))           # 30 출력
print(super_add(1, 2, 3, 4, 5, 6)) # 21 출력 (몇 개든 끄떡없습니다)