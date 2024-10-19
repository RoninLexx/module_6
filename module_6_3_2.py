class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        Horse.x_distance = Horse.x_distance + dx

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        Eagle.y_distance = Eagle.y_distance + dy

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (Horse.x_distance, Eagle.y_distance)

    def voice(self):
        # первый вариант
        # print(Eagle.sound)
        # второй вариант
        second_creature_class = Pegasus.__bases__[1]
        second_creature_instance = second_creature_class()
        print(second_creature_instance.sound)




if __name__ == '__main__':
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()

