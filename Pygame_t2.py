# -*- coding: utf-8 -*-
# Clone coding
import pygame

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [400, 900]
screen = pygame.display.set_mode(size)

title = "My Game"
pygame.display.set_caption(title)

# 3. 게임내 필요한 설정
clock = pygame.time.Clock()
spaceship = pygame.image.load(
    "C:/Users/82108/Desktop/workspace/image/spaceship.png").convert_alpha()
spaceship = pygame.transform.scale(spaceship, (50, 80))

spaceship_x1, spaceship_y1 = spaceship.get_size()
spaceship_x2 = round(size[0] / 2) - spaceship_x1 / 2
spaceship_y2 = size[1] - spaceship_y1 - 15


black = (0, 0, 0)
white = (255, 255, 255)

# 4. 메인 이벤트
SB = 0
while SB == 0:

    # 4-1, FPS 설정
    clock.tick(60)

    # 4-2, 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1

    # 4-3, 입력, 시간에 따른 변화

    # 4-4, 그리기
    screen.fill(black)
    screen.blit(spaceship, (spaceship_x2, spaceship_y2))
    # 4-5, 업데이트
    pygame.display.flip()

# 5 게임종료
pygame.quit()
