class Animal:
    def __init__(self, name, color, age, sex):
        self.action="会跑"
        self.sound = "会叫"
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def Sound(self):
        print(self.sound)

    def Action(self):
        print(self.action)

if __name__ == '__main__':
    dongwu = Animal()
    dongwu.Action()
    dongwu.Sound()
