from settings import *
import pygame as pg
import math


class Camera:
    def __init__(self, render):
        self.render = render
        self.x, self.y = CAMERA_POS
        self.angle = CAMERA_ANGLE
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = CAMERA_SPEED * self.render.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            
            dx += -speed_sin
            dy += speed_cos
        

        self.check_wall_collision(dx,dy)
        
        self.angle %= math.tau
    def check_wall(self, x, y):
        return (x, y) not in self.render.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = CAMERA_SIZE_SCALE / self.render.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
    def draw(self):
        pg.draw.line(self.render.screen, 'yellow', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH * math.cos(self.angle),
                      self.y * 100 + WIDTH * math. sin(self.angle)), 2)
        pg.draw.circle(self.render.screen, 'green', (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.render.delta_time

    def update(self):
        self.movement()
        self.mouse_control()
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)