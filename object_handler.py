from sprite_object import *

class ObjectHandler:
    def __init__(self,render):
        self.render = render
        self.sprite_list = []
        self.static_sprite_path = 'obrazkispriteBomba/exp1.png'
        self.add_sprite_path = 'obrazkispriteBomba/exp1.png'

        add_sprite = self.add_sprite

        
        add_sprite(AnimatedSprite(render))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self,sprite):
        self.sprite_list.append(sprite)