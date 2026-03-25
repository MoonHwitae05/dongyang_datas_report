def factorial(n):
    # 1. 절대 잊어선 안되는 브레이크 (Base Case)
    if n <= 0:
        return 1 
    
    # 2. 크기(n)를 1칸씩 줄여가며 자기 자신을 향해 끝없이 다이브합니다.
    return n * factorial(n - 1) 

print("3 팩토리얼의 결과:", factorial(3))