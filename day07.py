class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성됩니다:', end=' ')

    def info(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬목록 중 하나 선택')
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')
        # for skill in self.skills:
        #     print(f'{skill}')

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전')


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner,skills)
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')


class Ggobugi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):   # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')

    def swim(self):
        print(f'{self.name} 수영')


class Pairi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')


while True:
    menu = input('1) 포켓몬 생성  2) 프로그램 종료: ')
    if menu == '2':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        pokemon = input('1) 피카츄  2) 꼬부기  3) 파이리: ')
        if pokemon  == '1':
            n = input('플레이어 이름을 입력하세요 : ')
            s = input('사용 가능한 기술 입력(/로 구분하여 입력하시오):  ')
            p = Pikachu(n, s)
        elif pokemon  == '2':
            n = input('플레이어 이름을 입력하세요 : ')
            s = input('사용 가능한 기술 입력(/로 구분하여 입력하시오):  ')
            p = Ggobugi(n, s)
        elif pokemon  == '3':
            n = input('플레이어 이름을 입력하세요 : ')
            s = input('사용 가능한 기술 입력(/로 구분하여 입력하시오):  ')
            p = Pairi(n, s)
        else:
            print('잘못 입력하셨습니다!')
        info_attack = input('1) 정보조회  2) 공격  :  ')

        if info_attack == '1':
            p.info()
        elif info_attack == "2":
            p.info()
            attack_menu = input('공격 번호 선택: ')
            p.attack(int(attack_menu)-1)
        else:
            print('잘못 입력하셨습니다')

    else:
        print('잘못 입력하셨습니다!')


# pk1 = Pikachu('지우','전광석화/백만볼트')
# ggo1 = Ggobugi('오바람','고속스핀/거품/울기')
# # pk1.info()
# # ggo1.info()
# pk1.attack(0)
# ggo1.attack(0)
#
# p0 = Pokemon('아이리스', '의문의 공격스킬')
# p0.attack(0)
# ggo1.swim() # 꼬부기 클래스의 객체만 사용할 수 있음