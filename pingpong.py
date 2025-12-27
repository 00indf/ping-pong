from pygame import *

mainwin = display.set_mode((600, 400))
display.set_caption('Ping Pong')
bg = transform.scale(image.load('table.png'), (700, 700))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mainwin.blit(self.image, (self.rect.x, self.rect.y))

ball = GameSprite('ball.png', 280, 180, 40, 40, 5)

clock = time.Clock()
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        mainwin.blit(bg, (-50, -150))
        ball.reset()
    display.update()
    clock.tick(60)