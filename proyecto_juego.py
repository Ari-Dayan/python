import pygame,sys,os, random

pygame.init

player_leng = 100
player_heigh = 70


background =pygame.transform.scale(pygame.image.load(os.path.join("assets", "espacio_pixelart.jpg")), (1000, 800))






BLACK =(0, 0, 0 )
ventana = (1000, 800)
done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode(ventana)
score = 0


pygame.mouse.set_visible(0)



class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale (pygame.image.load(os.path.join("assets", "nave_pixelart.png")), (player_leng, player_heigh))
        self.rect = self.image.get_rect()
#esta es la clase de los meteoros, definimos la skin y la posicion_____________________________________________________________________________________________________________________
class Meteor(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        meteor_size = random.randrange(20,50)
        self.image = pygame.transform.scale (pygame.image.load(os.path.join("assets", "meteoro_pixelart.png")), (meteor_size,meteor_size ))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

#estas son las listas que guardan la informacion del meteoro__________________________________________________________________________________________________________________________________________________________________________________________________________________________
meteor_list = pygame.sprite.Group()
all_sprite = pygame.sprite.Group()



#en este for crean al meteoro_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________x
for i in range (50):
    meteor= Meteor()
    meteor.rect.x = random.randrange(ventana[0]-30)
    meteor.rect.y = random.randrange(ventana[1]-30)

    meteor_list.add(meteor)
    all_sprite.add(meteor)
    
player = Player()
all_sprite.add(player)

#el bucle main______________________________________________________________________________________________________________________________________________________________________________
while not done:
    
     
    if random.randrange(35) == 4:

        meteor= Meteor()
        meteor.rect.x = random.randrange(ventana[0]-30)
        meteor.rect.y = random.randrange(ventana[1]-30)
        meteor_list.add(meteor)
        all_sprite.add(meteor)  
        
        
    clock.tick(60)

    all_sprite.draw(screen)

    pygame.display.flip()
    # esta funcion es para cuando dos sprite se choquen _______________________________________________________________________________________________________________________________
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
    # esta funcion es para cuando dos sprite se choquen _______________________________________________________________________________________________________________________________
    for event in pygame.event.get():

        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]
      

        if event.type == pygame.QUIT:
           sys.exit()
    
 
    for meteor in meteor_hit_list:
        score += 1
        print (score)
    
    screen.blit(background, [0,0])

    
