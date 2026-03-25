def make_profile(**kwargs):
    print(f"이름: {kwargs.get('name')}, 나이: {kwargs.get('age')}, 직업: {kwargs.get('job')}")

make_profile(job="해커", name="앨리스", age=25)