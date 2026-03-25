def create_hero(name, **kwargs):
    print(f"\\n--- 영웅 {name} 탄생 ---")
    # kwargs는 이제 {'hp': 100, 'mp': 50, 'weapon': 'Sword'} 라는 딕셔너리가 되었습니다!
    for key, value in kwargs.items():
        print(f" [{key}] 능력치: {value}")

# hp, mp, weapon 등 내가 원하는 스탯을 무한대로 이름 붙여서 마음껏 던질 수 있습니다!
create_hero("아서", hp=1000, mp=50, weapon="엑스칼리버")