import pygame as pg
import math
import bar

pg.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

running = True
player_pos = pg.Vector2(screen.get_width() / 10, screen.get_height() / 2.2)
enemy_pos = pg.Vector2(screen.get_width() / 1.1, screen.get_height() / 2.2)
player_color = "yellow"
enemy_color = "red"
ball_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_vel = pg.Vector2(-300, 250)
ball_color = "white"
ball_radius = 14  

bar1_pos = pg.Vector2(0, 0)
bar2_pos = pg.Vector2(0, screen.get_height())
end_color = "black"

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    dt = clock.tick(60) / 1000

    keys = pg.key.get_pressed()
    if keys[pg.K_w] and player_pos.y > 0:
        player_pos.y -= 250 * dt
    if keys[pg.K_s] and player_pos.y < screen.get_height() - 100:
        player_pos.y += 250 * dt

    if keys[pg.K_UP] and enemy_pos.y > 0:
        enemy_pos.y -= 250 * dt
    if keys[pg.K_DOWN] and enemy_pos.y < screen.get_height() - 100:
        enemy_pos.y += 250 * dt

    ball_pos += ball_vel * dt

    if ball_pos.y - ball_radius <= 0 or ball_pos.y + ball_radius >= screen.get_height():
        ball_vel.y = -ball_vel.y

    if ball_pos.x - ball_radius <= 0 or ball_pos.x + ball_radius >= screen.get_width():
        running = False

    player_rect = bar.conf(screen, player_color, player_pos)
    if bar.check_ball_collision_with_rect(ball_pos, ball_radius, player_rect):
        ball_vel.x = -ball_vel.x

    enemy_rect = bar.conf(screen, enemy_color, enemy_pos)
    if bar.check_ball_collision_with_rect(ball_pos, ball_radius, enemy_rect):
        ball_vel.x = -ball_vel.x

    screen.fill("black")

    bar.conf(screen, player_color, player_pos)
    bar.conf(screen, enemy_color, enemy_pos)

    pg.draw.circle(screen, ball_color, (int(ball_pos.x), int(ball_pos.y)), ball_radius)

    bar.conf2(screen, end_color, bar1_pos, 5, screen.get_height())
    bar.conf2(screen, end_color, bar2_pos, 5, screen.get_height())

    pg.display.flip()

pg.quit()
