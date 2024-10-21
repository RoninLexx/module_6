import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Бум-Хрясь"

class Background(arcade.Sprite):
    def __init__(self):
        super().__init__('background1.png', 1.2)

class Brick(arcade.Sprite):
    def __init__(self):
        super().__init__('element_grey_rectangle.png', 1.0)

class Brickbrake(arcade.Sprite):
    def __init__(self):
        super().__init__('fatia6Hi2.png', 1.0)


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball-6x6.png', 1.0)
        self.change_x = 2
        self.change_y = 2

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = self.change_x = 0


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('Paddle.png', 1.0)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = Background()
        self.brick1 = Brick()
        self.brick2 = Brick()
        self.br_bl1 = Brickbrake()
        self.br_bl2 = Brickbrake()
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.background.center_x = SCREEN_WIDTH / 2
        self.background.center_y = SCREEN_HEIGHT / 2
        self.brick1.center_x = SCREEN_WIDTH / 1.5
        self.brick1.center_y = SCREEN_HEIGHT / 1.5
        self.brick2.center_x = SCREEN_WIDTH / 1.8
        self.brick2.center_y = SCREEN_HEIGHT / 1.8
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 10
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 9


    def on_draw(self):
        self.background.draw()
        self.brick1.draw()
        self.brick2.draw()
        self.br_bl1.draw()
        self.br_bl2.draw()
        self.bar.draw()
        self.ball.draw()




    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.bottom = self.bar.top
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()
        if arcade.check_for_collision(self.ball, self.brick1):
            self.ball.change_y = -self.ball.change_y
            self.brick1 = self.br_bl1
            self.br_bl1.center_x = SCREEN_WIDTH / 1.5
            self.br_bl1.center_y = SCREEN_HEIGHT / 1.5
        self.ball.update()
        if arcade.check_for_collision(self.ball, self.brick2):
            self.ball.change_y = -self.ball.change_y
            self.brick2 = self.br_bl2
            self.br_bl2.center_x = SCREEN_WIDTH / 1.8
            self.br_bl2.center_y = SCREEN_HEIGHT / 1.8
        self.ball.update()
        if arcade.check_for_collision(self.ball, self.br_bl1):
            self.ball.change_y = -self.ball.change_y

        self.ball.update()
        if arcade.check_for_collision(self.ball, self.br_bl2):
            self.ball.change_y = -self.ball.change_y

        self.ball.update()



    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 6
        if key == arcade.key.LEFT:
            self.bar.change_x = -6

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
