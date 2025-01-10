from pygame import*
from pytmx import*

WINDOW_WIDTH=930
WINDOW_HEIGTH=930

TILE_SIZE=32

win=display.set_mode((WINDOW_WIDTH,WINDOW_HEIGTH))

clock=time.Clock() 

class Sprite(sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image=transform.scale(surf,(TILE_SIZE,TILE_SIZE))
        self.rect=self.image.get_rect(topleft=pos)

class ObjectsSprite(sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_rect(topleft=pos)

all_sprites=sprite.Group()
object_sprites=sprite.Group()
collision_sprites=sprite.Group()
def setup():
    map=load_pygame('map.tmx')

    for x,y,image in map.get_layer_by_name('Вотер').tiles():
        Sprite((x*TILE_SIZE,y*TILE_SIZE),image,all_sprites)
    
    
    for x,y,image in map.get_layer_by_name('Іленд').tiles():
        Sprite((x*TILE_SIZE,y*TILE_SIZE),image,all_sprites)
    
    for x,y,image in map.get_layer_by_name('Бріджі').tiles():
        Sprite((x*TILE_SIZE,y*TILE_SIZE),image,all_sprites)
    
    
   
    
            
setup()

run=True

while run:
    for e in event.get():
        if e.type == QUIT:
            run=False
    all_sprites.update()
    object_sprites.update()
    collision_sprites.update()
    all_sprites.draw(win)
    object_sprites.draw(win)
    collision_sprites.draw(win)

    display.update()
    clock.tick(60)