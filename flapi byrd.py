

from pygame import *
from random import randint

init()
window_size = 1200, 800
window = display.set_mode(window_size)
clock = time.Clock()

player_rect = Rect(150, window_size[1] // 2 - 100, 100, 100)


def generate_pipes(count, pipe_width=140, gap=280, min_height=50, max_height=440, distance=650):
    pipes = []
    start_x = window_size[0]
    for i in range(count):
        height = randint(min_height, max_height)
        top_pipe = Rect(start_x, 0, pipe_width, height)
        bottom_pipe = Rect(start_x, height + gap, pipe_width, window_size[1] - (height + gap))
        pipes.extend([top_pipe, bottom_pipe])
        start_x += distance
    return pipes


pipes = generate_pipes(150)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            quit()

    window.fill('sky blue')
    draw.rect(window, 'blue', player_rect)
    if len(pipes) < 8:
        pipes += generate_pipes(150)

    for pipe in pipes:
        pipe.x -= 10
        draw.rect(window, 'green', pipe)
        if pipe.x <= -100:
            pipes.remove(pipe)
        if player_rect.colliderect(pipe):
            game = False

    keys = key.get_pressed()
    if keys[K_s]:
        player_rect.y += 5
    if keys[K_w]:
        player_rect.y -= 5

    display.update()
    clock.tick(60)