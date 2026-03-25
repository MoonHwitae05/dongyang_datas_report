class Robot:
    # 파이썬 특수 매직 메서드 (양쪽 언더바 2개)
    # 로봇() 을 찍어내는 순간 무조건 제일 먼저 은밀하게 실행됩니다!
    def __init__(self, name, color):
        self.name = name   # 이 로봇의 명찰에 외부에서 받아온 name을 적습니다.
        self.color = color # 이 로봇의 도색을 외부에서 받아온 color로 칠합니다.
        print(f"삐릭! [{self.name}] 로봇({self.color}색) 초기화 완료!")

# 괄호 안에 값을 넘겨주면, 그 값들이 __init__ 메서드로 곧장 빨려 들어갑니다.
robot1 = Robot("R2D2", "White/Blue")
robot2 = Robot("C3PO", "Gold")

# robot1.name 은 R2D2, robot2.name 은 C3PO로 완벽히 격리된 데이터를 가집니다.