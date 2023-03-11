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
pos = 0


pygame.mouse.set_visible(0)



class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale (pygame.image.load(os.path.join("assets", "nave_pixelart.png")), (player_leng, player_heigh))
        self.rect = self.image.get_rect()
        


class Projectil (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale (pygame.image.load(os.path.join("assets", "projectil.png")), (19, 47))
        self.rect = self.image.get_rect()

       
        
    def pum (self, pos):
        self.rect.y -=7
        all_sprite.add(projectil)
        self.rect.x = pos [0] + player_leng/2 - 9
        self.rect.y = pos [1]
    def update (self):
        self.rect.y -=7  
        
#esta es la clase de los meteoros, definimos la skin y la posicion_____________________________________________________________________________________________________________________
class Meteor(pygame.sprite.Sprite):    
    def __init__(self):
        
        super().__init__()
        meteor_size = random.randrange(20,50)
        self.image = pygame.transform.scale (pygame.image.load(os.path.join("assets", "meteoro_pixelart.png")), (meteor_size,meteor_size ))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    #en esta funcion se updatea la posicion de los meteoros 
    def update (self):
        self.rect.y +=1
        if self.rect.y == 800:
            self.rect.y = -50
            self.rect.x = random.randrange(0, 1000)


#estas son las listas que guardan la informacion de los meteoros y todos los sprites en pantalla__________________________________________________________________________________________________________________________________________________________________________________________________________________________
projectil_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
all_sprite = pygame.sprite.Group()



#en este for crean al meteoro_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________x
for i in range (50):
    meteor= Meteor()
    #elegimos las valores posibles de x e y en los que puede spawnear
    meteor.rect.x = random.randrange(ventana[0]-30)
    meteor.rect.y = random.randrange(ventana[1]-30)
    # este es el comandop que crea el objeto del meteoro y le da un sprite
    meteor_list.add(meteor)
    all_sprite.add(meteor)


#creamos al jugador utilizando la clase Player y al projectil utilizando Projectil
player = Player()
all_sprite.add(player)






projectil = Projectil()
#el bucle main______________________________________________________________________________________________________________________________________________________________________________
while not done:   
    
    
    #llamamos a la funcion para que los meteorosse muevan
    all_sprite.update()
    

    if random.randrange(35) == 4:

        meteor= Meteor()
        meteor.rect.x = random.randrange(ventana[0]-30)
        meteor.rect.y = -50
        meteor_list.add(meteor)
        all_sprite.add(meteor)  
        
    clock.tick(60)
    all_sprite.draw(screen)

    pygame.display.flip()
    # esta funcion es para cuando dos sprite se choquen _______________________________________________________________________________________________________________________________
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
    meteor_hit_list = pygame.sprite.spritecollide(projectil, meteor_list, True)
    projectil_hit_list = pygame.sprite .spritecollide(meteor, projectil_list,True)
    # esta funcion es para cuando dos sprite se choquen _______________________________________________________________________________________________________________________________
    
    for event in pygame.event.get():

        mouse_pos = pygame.mouse.get_pos()
        
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                projectil = Projectil()
                projectil_list.add(projectil)
                all_sprite.add(projectil)
                pos = mouse_pos
                projectil.pum(pos)
         
        if event.type == pygame.QUIT:
           sys.exit()
    

    screen.blit(background, [0,0])

    
