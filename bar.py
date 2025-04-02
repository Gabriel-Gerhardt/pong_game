import pygame as pg
import math 



def conf(screen, color, pos):
    # Adjust the size of the rectangle for a more appropriate bar size
    bar_width = 20
    bar_height = 100
    
    rect = pg.Rect(pos.x, pos.y, bar_width, bar_height)
    
    # Draw the rectangle (bar) on the screen
    pg.draw.rect(screen, color, rect)
    return rect


def conf2(screen, color, pos,width, height):
    # Adjust the size of the rectangle for a more appropriate bar size
    bar_width = width
    bar_height = height
    
    rect = pg.Rect(pos.x, pos.y, bar_width, bar_height)
    
    # Draw the rectangle (bar) on the screen
    pg.draw.rect(screen, color, rect)
    return rect


def check_ball_collision_with_rect(ball_pos, ball_radius, rect):
    # Get the closest point on the rectangle to the ball
    closest_x = max(rect.left, min(ball_pos[0], rect.right))
    closest_y = max(rect.top, min(ball_pos[1], rect.bottom))
    flag =False
    # Calculate the distance between the ball's center and the closest point on the rectangle
    distance = math.sqrt((closest_x - ball_pos[0]) ** 2 + (closest_y - ball_pos[1]) ** 2)

    # If the distance is less than or equal to the ball's radius, a collision occurs
    if(distance<=ball_radius):
        flag = True
    
    return flag