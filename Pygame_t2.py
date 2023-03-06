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
spaceship = pygame.image.load(
    "C:/Users/82108/Desktop/workspace/image/spaceship.png").convert_alpha()
spaceship = pygame.transform.scale(spaceship, (50, 80))

spaceship_x1, spaceship_y1 = spaceship.get_size()
spaceship_x2 = round(size[0] / 2) - spaceship_x1 / 2
spaceship_y2 = size[1] - spaceship_y1 - 15


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
    screen.blit(spaceship, (spaceship_x2, spaceship_y2))
    # 4-5, ������Ʈ
    pygame.display.flip()

# 5 ��������
pygame.quit()
