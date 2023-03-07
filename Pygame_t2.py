# -*- coding: utf-8 -*-
# Clone coding
import pygame

# 1. ���� �ʱ�ȭ
pygame.init()

# 2. ����â �ɼ� ����
size = [400, 900]
screen = pygame.display.set_mode(size)

title = "My Game"
pygame.display.set_caption(title)

# 3. ���ӳ� �ʿ��� ����
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0

    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x, self.y))

ss = obj()
ss.put_img("C:/Users/82108/Desktop/workspace/image/spaceship.png")
ss.change_size(50, 80)

ss.x = round(size[0] / 2 - ss.sx / 2)
ss.y = size[1] - ss.sy - 15


black = (0, 0, 0)
white = (255, 255, 255)

# 4. ���� �̺�Ʈ
SB = 0
while SB == 0:

    # 4-1, FPS ����
    clock.tick(60)

    # 4-2, ���� �Է� ����
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1

    # 4-3, �Է�, �ð��� ���� ��ȭ

    # 4-4, �׸���
    screen.fill(black)
    ss.show()

    # 4-5, ������Ʈ
    pygame.display.flip()

# 5 ��������
pygame.quit()
