"""比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】"""
from test.作业 import Animal


class Cat(Animal):
    def __init__(self, name="猫", color="棕色", age="2", sex="公"):
        self.hair = "短毛"
        super().__init__(name, color, age, sex)

    def Action2(self):
        print(f"{self.name}会捉老鼠,它的颜色是{self.color},它今年{self.age}岁了,它是{self.hair}猫")

    def Sound(self):
        self.sound = "喵喵叫"
        print(f"{self.name}会{self.sound}")


if __name__ == '__main__':
    cat = Cat()
    cat.Action2()
    cat.Sound()
