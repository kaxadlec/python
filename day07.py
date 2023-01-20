# class Person():
#     def __init__(self, name):
#         self.name = name
#
# class MDPerson():
#     def __init__(self,name):
#         self.name = "doctor " + name
# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name + ", Esquire"
#
# person = Person('mount')
# doctor = MDPerson('mount')
# lawyer = JDPerson('mount')
# print(doctor.name)

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성됩니다:', end=' ')

    def info(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬 .')
        for skill in self.skills:
            print(skill)

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전')

class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
       super().__init__(owner,skills)
       self.name = "피카츄"
       print(f"{self.name}")
    def attack(self, idx):  #override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')
class Ggobugi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
       super().__init__(owner, skills)
       self.name = "꼬부기"
       print(f"{self.name}")
    def attack(self, idx):   #override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')
    def swim(self):
        print(f'{self.name} 수영')

pk1 = Pikachu('지우','전광석화/백만볼트')
ggo1 = Ggobugi('오바람','고속스핀/거품/울기')
# pk1.info()
# ggo1.info()
pk1.attack(0)
ggo1.attack(0)

p0 = Pokemon('아이리스', '의문의 공격스킬')
p0.attack(0)
ggo1.swim() # 꼬부기 클래스의 객체만 사용할 수 있음