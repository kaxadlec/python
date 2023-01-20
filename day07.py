class PreetyMixin():
    # def time_print(self):
    #     import datetime
    #     datetime.date.today
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PreetyMixin):
    pass

t = Thing()
t.name = "mudryk"
t.feature = "fw"
t.age = '20'
#t.time_print()
print(t.dump())
