def make_profile(name, age, job):
    print(f"이름: {name}, 나이: {age}, 직업: {job}")

# 1. 위치 인자 (순서대로 꽂힘 - 일반적 방식)
make_profile("앨리스", 25, "해커")

# 2. 키워드 인자 (순서를 무시하고 이름표로 저격하여 꽂음)
make_profile(job="해커", name="앨리스", age=25) 
# 결과는 완전히 똑같습니다! 