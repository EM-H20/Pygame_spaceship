# -*- coding: utf-8 -*-
import pygame

# 1.게임 초기화
pygame.init()

# 2.게임창 옵션 설정
size = [1000, 600]
screen = pygame.display.set_mode(size)

game_name = "run and jump game"
pygame.display.set_caption(game_name)

# 3.게임 내 필요한 옵션
clock = pygame.time.Clock()
black = (0, 0, 0)

# 4.메인 이벤트
SB = 0
while SB == 0:    
    # 4-1 FPS설정
    clock.tick(60)

    # 4-2 각종 입력설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1

    # 4-3 입력, 시간에 따른 변화

    # 4-4 그리기
    screen.fill(black)

    # 4-5 업데이트
    pygame.display.flip()

# 5.게임종료
pygame.quit()