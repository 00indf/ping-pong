from pygame import *

mainwin = display.set_mode((600, 400))
display.set_caption('Ping Pong')
bg = transform.scale(image.load('table.png'), (740, 1000))

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

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400 - 160:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400 - 160:
            self.rect.y += self.speed

ball = GameSprite('ball2.png', 280, 180, 40, 40, 3)
p1 = Player('racket2.png', 0, 120, 90, 160, 5)
p2 = Player('racket2.png', 510, 120, 90, 160, 5)

font.init()
font = font.Font(None, 70)
p1_win = font.render('Player 1 wins!', True, (255, 255, 255))
p2_win = font.render('Player 2 wins!', True, (255, 255, 255))
speed_x = 3
speed_y = 3
clock = time.Clock()
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        mainwin.blit(bg, (-70, -300))
        ball.reset()
        p1.reset()
        p2.reset()
        p1.update_l()
        p2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.x < 0:
            mainwin.blit(p2_win, (150, 175))
            finish = True
        if ball.rect.x > 560:
            mainwin.blit(p1_win, (150, 175))
            finish = True
        if ball.rect.y > 400 - 40 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_x *= -1
    display.update()
    clock.tick(60)
