# -*- coding: utf-8 -*-
import pygame

# 1.���� �ʱ�ȭ
pygame.init()

# 2.����â �ɼ� ����
size = [1000, 600]
screen = pygame.display.set_mode(size)

game_name = "run and jump game"
pygame.display.set_caption(game_name)

# 3.���� �� �ʿ��� �ɼ�
clock = pygame.time.Clock()
black = (0, 0, 0)

# 4.���� �̺�Ʈ
SB = 0
while SB == 0:    
    # 4-1 FPS����
    clock.tick(60)

    # 4-2 ���� �Է¼���
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1

    # 4-3 �Է�, �ð��� ���� ��ȭ

    # 4-4 �׸���
    screen.fill(black)

    # 4-5 ������Ʈ
    pygame.display.flip()

# 5.��������
pygame.quit()