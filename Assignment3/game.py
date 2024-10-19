import pygame
import random
import sys
import math

pygame.init()

# 设置窗口大小
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇")

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
pink = (255, 182, 193)  # 粉红色

# 蛇的初始位置和大小
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]  # 初始蛇身由3个部分组成

# 食物的初始位置
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# 初始速度和方向
speed = 15
direction = 'RIGHT'
change_to = direction

# 计分
score = 0

# 绘制爱心形状的函数
def draw_heart(color, center, size):
    x, y = center
    heart_points = [
        (x, y + size), 
        (x - size * 0.5, y + size * 0.5), 
        (x - size, y), 
        (x - size * 0.5, y - size * 0.5), 
        (x, y - size), 
        (x + size * 0.5, y - size * 0.5), 
        (x + size, y), 
        (x + size * 0.5, y + size * 0.5)
    ]
    pygame.draw.lines(screen, color, False, heart_points, 2)

# 游戏主循环
while True:
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'

    # 确保蛇不能直接逆向移动
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # 移动蛇头
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10

    # 蛇身增长机制
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
    
    # 食物生成
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # 绘制背景和蛇
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, pink, pygame.Rect(pos[0], pos[1], 10, 10))  # 使用粉红色绘制蛇的身体
    draw_heart(white, food_pos, 10)  # 使用爱心形状绘制食物

    # 游戏结束条件
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        pygame.quit()
        sys.exit()
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        pygame.quit()
        sys.exit()
    for block in snake_body[1:]:
        if snake_pos == block:
            pygame.quit()
            sys.exit()

    # 刷新屏幕和设置帧率
    pygame.display.update()
    pygame.time.Clock().tick(speed)

# 退出 Pygame
pygame.quit()