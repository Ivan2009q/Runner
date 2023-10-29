
from pygame import *
window = display.set_mode((700, 500))
display.set_caption("догонялки")
background = transform.scale(image.load("background.jpg"),(700, 500))
class GameSprite(sprite.Sprite):
     def __init__(self,player_image, player_x, player_y, player_speed):
          super().__init__()
          self.image = transform.scale(image.load(player_image),(65,65))
          self.speed = player_speed
          self.rect = self.image.get_rect()
          self.rect.x = player_x
          self.rect.y = player_y
     def reset(self):
          window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
     def update(self):
          keys = key.get_pressed()
          if keys[K_LEFT] and self.rect.x > 5:
               self.rect.x -=self.speed
          if keys[K_RIGHT] and self.rect.x < win_width - 80:
               self.rect.x += self.speed
          if keys[K_UP] and self.rect.y >5:
               self.rect.y -= self.speed
          if keys [K_DOWN] and self.rect.y< win_height - 80:
               self.rect.y += self.speed


class Wall (sprite.Sprite):
     def __init__(self,color_1,color_2,color_3, wall_x, wall_y, wall_width,wall_height):
          super().__init__()
          self.color_1 = color_1
          self.color_2 = color_2
          self.color_3 = color_3
          self.width = wall_width
          self.height = wall_height
          self.image = Surface((self.width, self.height))
          self.image.fill((color_1, color_2, color_3))
          self.rect = self.image.get_rect()
          self.rect.x = wall_x
          self.rect.y = wall_y
     def draw_wall(self):
          window.blit(self.image,( self.rect.x,self.rect.y))     



win_width = 700
win_height = 500
player = Player('hero.png', 5, win_height - 80, 4)
monster = GameSprite('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
w1= Wall(57,87,100,100,100,450,10)
w2= Wall(53,73,89,99,99,425,11)
clock= time.Clock()
FPS=60
game = True 
finish=False
while game:
     for e in event.get():
          if e.type == QUIT:
               game = False
     if finish != True:
          if sprite.collide_rect(player,final):
               finish = True
     window.blit(background,(0, 0 ))
     player.update()
     monster.update

     player.reset()
     monster.reset()
     final.reset() 

     w1.draw_wall()
     w2.draw_wall()
     display.update()
     clock.tick(FPS)