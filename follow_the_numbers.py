import pgzrun
from pgzero.builtins import *
from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
next_dot = 0

for _ in range(10):
    actor = Actor('dot')
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 36)
    dots.append(actor)


def draw():
    screen.fill('black')
    for number, dot in enumerate(dots, start=1):
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()

    for start, end in lines:
        screen.draw.line(start, end, (100, 0, 0))


def on_mouse_down(pos):
    global next_dot, lines

    # Start a new round on the next click after all dots are connected.
    if next_dot >= len(dots):
        lines = []
        next_dot = 0
        return

    if dots[next_dot].collidepoint(pos):
        if next_dot > 0:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot += 1
    else:
        lines = []
        next_dot = 0


pgzrun.go()
