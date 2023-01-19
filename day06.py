# class
# class Pokemon:
#     def __init__(self):
#         print("포켓몬 객체 생성된다")
# p1 = Pokemon()  # 포켓몬 객체 생성된다
# p2 = Pokemon()  # 포켓몬 객체 생성된다
# print(p1,p2)  # <__main__.Pokemon object at 0x000002497832C6D0> <__main__.Pokemon object at 0x000002497832C750>

# class Pokemon:
#     def __init__(self, name):
#         self.name = name
#         print(f'{name} 생성')
#
# p1 = Pokemon('파이리')
# p2 = Pokemon('고라파덕')
# print(p1.name,p2.name)

# class Pokemon:
#     def __init__(self, name, owner):
#         self.name = name
#         self.owner = owner
#         print(f'{name} 생성')
#
# p1 = Pokemon('파이리', '빛나')
# p2 = Pokemon('고라파덕', '지우')
# print(f'{p1.owner}는 {p1.name}를 선택했다.')
# print(f'{p2.owner}는 {p2.name}를 선택했다.')

class Pokemon:
    def __init__(self, name, owner,skills):
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f'{name} 생성')

    def info(self):
        print(f'{self.owner}의 포켓몬은 {self.name}입니다.')
        for skill in self.skills:
            print(skill)

#p1 = Pokemon('파이리', '빛나', '불꽃세례/회오리불꽃/화염방사')
p2 = Pokemon('고라파덕','지우','할퀴기/꼬리흔들기/물대포')
# p1.info()
p2.info()
# print(p1.skills)