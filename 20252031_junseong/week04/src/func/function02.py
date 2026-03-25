# country="한국" 이라는 디폴트(기본) 방어막을 쳐두었습니다.
def make_passport(name, country="한국"):
    print(f"{name}님의 여권 발행 국가는 [{country}] 입니다.")

make_passport("김철수")               # 아무것도 안 넣으면 '한국' 무혈 입성
make_passport("James", "미국")       # 명시적으로 '미국'을 던지면 한국을 밀어내고 덮어씀