"""
Project Name: Submarine Sabotage
By: Jonathan Murphy
Date: 2/20/2019
Description: Two player arcade game with the objective of firing
missiles to kill the enemy sub.

"""

import sys, pygame, time, math, os
from pygame.sprite import Sprite

# controls the delay in between frames to slow down the sub
speed = 0
# controls the number of pixles a sub can move each turn
fuel = 400
# controls whos turn in is
turn = 1
# holds who has fired
fireusa = False
fireussr = False
uhit = 5
rhit = 5
#holds time value
gametime = 0
#holds angle value
angle = 0
#holds health values
subusahealth = 3
subussrhealth = 3
#unlocks hidden gamemode
snek = False
ussrsong = False



"""settings.py"""
################################################################

class Settings():
    """ A class to store all the settings for submarine sabotage"""
        
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1500
        self.screen_height = 750
        self.bg_color = (213,234,248)

"""background.py"""
################################################################

class Background():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/backgroundgraph.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def blitme(self):
        """Draw sub at it's current location"""
        self.screen.blit(self.image, self.rect)
    
"""sub.py"""
################################################################

"""United States submarine"""
class Subusa():
    def __init__(self,screen):
        """initialize the sub and it's starting position"""
        self.screen = screen

        #load the sub image and get its rect.
        self.image = pygame.image.load('images/subusa.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #starting position
        self.rect.left = self.screen_rect.left + 100
        self.rect.bottom = self.screen_rect.bottom -200

        #movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        global fireusa
        global fuel
        global turn
        
        #if they have fired they can't move
        if (fireusa):
            fuel = 0 

        #if they haven't fired they can move
        if (fuel > 0 and turn == 1):
            if self.moving_right and self.rect.left < self.screen_rect.right - 80:
                if (self.rect.bottom < int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                    self.rect.left +=1
                    fuel -= 1
                else:
                    if(self.rect.bottom > int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                        self.rect.left -=2
                        fuel -= 2

                
            if self.moving_left and self.rect.left > self.screen_rect.left:
                if (self.rect.bottom < int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                    self.rect.left -=1
                    fuel -= 1
                else:
                    if(self.rect.bottom > int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                        self.rect.left +=2
                        fuel -= 2
                        
            if self.moving_up and self.rect.bottom > self.screen_rect.top + 30:
                self.rect.bottom -=1
                fuel -= 1
                    
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                if (self.rect.bottom < int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                    self.rect.bottom +=1
                    fuel -= 1
                else:
                    if(self.rect.bottom > int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                        self.rect.bottom -=2
                        fuel -=2
                    

    def blitme(self):
        global subusahealth
        healthu3 = pygame.image.load('images/healthu3.png').convert_alpha()
        healthu2 = pygame.image.load('images/healthu2.png').convert_alpha()
        healthu1 = pygame.image.load('images/healthu1.png').convert_alpha()
        
        """Draw sub at it's current location"""
        self.screen.blit(self.image, self.rect)

        if (subusahealth == 3):
            self.screen.blit(healthu3, (10,50))
            self.screen.blit(healthu2, (68,51))
            self.screen.blit(healthu1, (114,52))
        elif (subusahealth == 2):
            self.screen.blit(healthu2, (68,51))
            self.screen.blit(healthu1, (114,52))
        elif (subusahealth == 1):
            self.screen.blit(healthu1, (114,52))
            


""" Sub USSR """
class Subussr():
    def __init__(self,screen):
        """initialize the sub and it's starting position"""
        self.screen = screen
        #load the sub image and get its rect.
        self.image = pygame.image.load('images/subussr.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #starting position
        self.rect.right = self.screen_rect.right - 100
        self.rect.bottom = self.screen_rect.bottom -200

        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        global fireussr
        global fuel
        global turn
        """ Update the subs position based on the movement flag"""

        if (fireussr):
            fuel = 0
        
        if (fuel > 0 and turn == 2):
            if self.moving_right and self.rect.left < self.screen_rect.right - 80:
                if (self.rect.bottom < int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                    self.rect.left +=1
                    fuel -= 1
                else:
                    if(self.rect.bottom > int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                        self.rect.left -=2
                        fuel -= 2

                
            if self.moving_left and self.rect.left > self.screen_rect.left:
                if (self.rect.bottom < int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                    self.rect.left -=1
                    fuel -= 1
                else:
                    if(self.rect.bottom > int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                        self.rect.left +=2
                        fuel -= 2
                        
            if self.moving_up and self.rect.bottom > self.screen_rect.top + 30:
                self.rect.bottom -=1
                fuel -= 1
                    
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                if (self.rect.bottom < int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                    self.rect.bottom +=1
                    fuel -= 1
                else:
                    if(self.rect.bottom > int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                        self.rect.bottom -=2
                        fuel -=2

    def blitme(self):
        global subussrhealth
        healthr3 = pygame.image.load('images/healthr3.png').convert_alpha()
        healthr2 = pygame.image.load('images/healthr2.png').convert_alpha()
        healthr1 = pygame.image.load('images/healthr1.png').convert_alpha()
        
        """Draw sub at it's current location"""
        self.screen.blit(self.image, self.rect)

        if (subussrhealth == 3):
            self.screen.blit(healthr3, (1440,50))
            self.screen.blit(healthr2, (1395,51))
            self.screen.blit(healthr1, (1339,52))
        elif (subussrhealth == 2):
            self.screen.blit(healthr2, (1395,51))
            self.screen.blit(healthr1, (1339,52))
        elif (subussrhealth == 1):
            self.screen.blit(healthr1, (1339,52))
################################################################
        
"""game_functions.py"""
################################################################
 
class Game_functions():

    def check_events(subusa, subussr):
        global fireusa
        global fireussr
        global turn
        """respond to keypresses and mouse events"""
        for event in pygame.event.get():
                # Close the game window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                # USA Movement
                elif event.type == pygame.KEYDOWN:
                    """USA movement"""
                    if event.key == pygame.K_d:
                        subusa.moving_right = True
                    elif event.key == pygame.K_a:
                        subusa.moving_left = True
                    if event.key == pygame.K_w:
                        subusa.moving_up = True
                    elif event.key == pygame.K_s:
                        subusa.moving_down = True
                    """USSR movement"""
                    if event.key == pygame.K_RIGHT:
                        subussr.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        subussr.moving_left = True
                    if event.key == pygame.K_UP:
                        subussr.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        subussr.moving_down = True
                    """torpedousa fire"""
                    if event.key == pygame.K_SPACE and turn == 1:
                        fireusa = True
                    """torpedousa fire"""
                    if event.key == pygame.K_SPACE and turn == 2:
                        fireussr = True

                elif event.type == pygame.KEYUP:
                    """USA movement"""
                    if event.key == pygame.K_d:
                        subusa.moving_right = False
                    elif event.key == pygame.K_a:
                        subusa.moving_left = False
                    if event.key == pygame.K_w:
                        subusa.moving_up = False
                    elif event.key == pygame.K_s:
                        subusa.moving_down = False
                    """USSR movement"""
                    if event.key == pygame.K_RIGHT:
                        subussr.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        subussr.moving_left = False
                    if event.key == pygame.K_UP:
                        subussr.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        subussr.moving_down = False
                

    def update_screen(ai_settings, screen, subusa, subussr, torpedousa, torpedoussr, aimusa, aimussr, background, text):
        """Update images on the screen and flip to the new screen"""
        global fireusa
        global fireussr
        global turn
        #redraw the screen during each pass through of the loop
        if(snek):
            if(True != fireusa and turn == 1):
                background.blitme()
            if(True != fireussr and turn == 2):
                background.blitme()

            subusa.blitme()
            aimusa.blitme()
            subussr.blitme()
            aimussr.blitme()
            torpedousa.blitme()
            torpedoussr.blitme()
            text.blitme()
            
            
        else:
            background.blitme()
            subusa.blitme()
            aimusa.blitme()
            subussr.blitme()
            aimussr.blitme()
            torpedousa.blitme()
            torpedoussr.blitme()
            text.blitme()

        #make the most recently drawn screen visible
        pygame.display.flip()

################################################################

"""bullet.py"""     
################################################################

class Torpedousa():
    # a class to manage bullets fired from the ship
   
    def __init__(self, screen, subusa, subussr):
        self.image = pygame.image.load('images/torpedousa.png').convert_alpha()
        line = pygame.image.load('images/aimusa.png')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.y = subusa.rect.bottom
        self.x = subusa.rect.right
        self.xspeed = 0
        self.yspeed = 0
        
        
        #boolean to store if subusa has fired
            
    def update(self, screen, subusa, subussr):
        global angle
        global fireusa
        global gametime
        global turn
        global fuel
        global subussrhealth
        global uhit

        #getting angle from aim and applying it to torpedo
        if(0 < angle and angle < 90):
            yspeed = - (math.sin(angle*(math.pi/180))*2)
            self.yspeed = yspeed + (gametime*.001)
            self.xspeed = 3
        elif(-90 < angle and angle < 0):
            yspeed = (abs(math.sin(angle*(math.pi/180)))*2)
            self.yspeed = yspeed - (gametime*.001)
            self.xspeed = 3

        #FIRE
        if(fireusa):
            explosion = pygame.mixer.Sound('sounds/explosion.wav')
            """move torpedo on the screen"""
            self.y = subusa.rect.bottom + (self.yspeed * gametime)
            self.x = subusa.rect.right + (self.xspeed * gametime)

            self.rect.y = self.y -15
            self.rect.x = self.x
            gametime += 1

            #Torpedo goes off screen
            if (self.rect.x > self.screen_rect.right):
                gametime = 0
                fireusa = False
                turn = 2
                fuel = 400
            elif (self.rect.y > int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                gametime = 0
                fireusa = False
                turn = 2
                fuel = 400
                
            #COLLISION

            elif((self.rect.x > subussr.rect.left) or (self.rect.x + 10 > subussr.rect.left )):
               if((self.rect.x < subussr.rect.right) or (self.rect.x + 10 < subussr.rect.right)):
                   if((self.rect.y > subussr.rect.top) or (self.rect.y + 3 > subussr.rect.top)):
                       if((self.rect.y < subussr.rect.bottom) or (self.rect.y + 3 < subussr.rect.bottom)):
                           subussrhealth -= 1
                           #print(subussrhealth)
                           gametime = 0
                           fireusa = False
                           turn = 2
                           fuel = 400
                           uhit = 0
                           explosion.play()
                           
                           

    def blitme(self):
        explosion1 = pygame.image.load('images/explosion1.png')
        explosion2 = pygame.image.load('images/explosion2.png')
        explosion3 = pygame.image.load('images/explosion3.png')
        explosion4 = pygame.image.load('images/explosion4.png')
        global uhit
        """Draw sub at it's current location"""
        if(fireusa):
            self.screen.blit(self.image, self.rect)

        #explosion
        elif(uhit < 5):
            if(uhit < 1):
                self.screen.blit(explosion1, self.rect)
                uhit += .3
               # print('artificial slow down1')
            if(uhit > 1 and uhit < 2):
                self.screen.blit(explosion2, self.rect)
                uhit += .2
               # print('artificial slow down2')
            if(uhit > 2 and uhit < 3):
                self.screen.blit(explosion3, self.rect)
                uhit += .2
               # print('artificial slow down3')
            if(uhit > 3 and uhit < 4):
                self.screen.blit(explosion4, self.rect)
                uhit += .2
               # print('artificial slow down4')
            if(uhit == 4 or uhit > 4):
                uhit = 5
                

class Torpedoussr():
    # a class to manage torpedos fired from the sub
      
    def __init__(self, screen, subussr, subusa):
        self.image = pygame.image.load('images/torpedoussr.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.y = subussr.rect.bottom
        self.x = subussr.rect.right
        self.xspeed = 0
        self.yspeed = 0

    def update(self, screen, subussr, subusa):
        global angle
        global fireussr
        global gametime
        global turn
        global fuel
        global subusahealth
        global rhit
        
        #gets angle from aim and applies it to torpedo
        if(-180 > angle and angle > -270):
            yspeed = - (math.sin(angle*(math.pi/180))*2)
            self.yspeed = yspeed + (gametime*.001)
            self.xspeed = 3
        elif(-90 > angle and angle > -180):
            yspeed = (abs(math.sin(angle*(math.pi/180)))*2)
            self.yspeed = yspeed - (gametime*.001)
            self.xspeed = 3

        #FIRE
        if(fireussr):
            explosion = pygame.mixer.Sound('sounds/explosion.wav')
            """move torpedo on the screen"""
            self.y = subussr.rect.bottom + (self.yspeed * gametime)
            self.x = subussr.rect.left - (self.xspeed * gametime)

            self.rect.y = self.y
            self.rect.x = self.x
            gametime += 1

            #torpedo goes off screen
            if (self.rect.x < self.screen_rect.left - 10):
                gametime = 0
                fireussr = False
                turn = 1
                fuel = 400
            elif (self.rect.y > int(abs(-80*(math.cos(.00838*self.rect.x))-640))):
                gametime = 0
                fireussr = False
                turn = 1
                fuel = 400

            #COLLISION
            elif((self.rect.x > subusa.rect.left) or (self.rect.x + 10 > subusa.rect.left )):
               if((self.rect.x < subusa.rect.right) or (self.rect.x + 10 < subusa.rect.right)):
                   if((self.rect.y > subusa.rect.top) or (self.rect.y + 3 > subusa.rect.top)):
                       if((self.rect.y < subusa.rect.bottom) or (self.rect.y + 3 < subusa.rect.bottom)):
                           subusahealth -= 1
                           #print(subusahealth)
                           gametime = 0
                           fireussr = False
                           turn = 1
                           fuel = 400
                           rhit = 0
                           explosion.play()
                


    def blitme(self):
        explosion1 = pygame.image.load('images/explosion1.png')
        explosion2 = pygame.image.load('images/explosion2.png')
        explosion3 = pygame.image.load('images/explosion3.png')
        explosion4 = pygame.image.load('images/explosion4.png')
        global rhit
        """Draw sub at it's current location"""
        if(fireussr):
            self.screen.blit(self.image, self.rect)

        #explosion
        elif(rhit < 5):
            if(rhit < 1):
                self.screen.blit(explosion1, self.rect)
                rhit += .3
               # print('artificial slow down1')
            if(rhit > 1 and rhit < 2):
                self.screen.blit(explosion2, self.rect)
                rhit += .2
               # print('artificial slow down2')
            if(rhit > 2 and rhit < 3):
                self.screen.blit(explosion3, self.rect)
                rhit += .2
               # print('artificial slow down3')
            if(rhit > 3 and rhit < 4):
                self.screen.blit(explosion4, self.rect)
                rhit += .2
               # print('artificial slow down4')
            if(rhit == 4 or rhit > 4):
                rhit = 5
        
        
        
        
################################################################

class Aimusa():
    def __init__(self, screen, subusa):
        global turn
        global fireusa
        self.image = pygame.image.load('images/aimusa.png')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.y = subusa.rect.centery
        self.x = subusa.rect.right
        self.original = self.image

    def update(self, screen, subusa):
        global angle
        if (turn == 1 and (True!=fireusa)):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #fix angle things
            if (mouse_x < subusa.rect.right):
                mouse_x = subusa.rect.right
                mouse_y = subusa.rect.bottom
            center = self.rect.center
            rotate = pygame.transform.rotate
            if(mouse_x == self.x):
                mouse_x = mouse_x + .1
            
            try:
                angle = (math.tan((self.y-mouse_y)/(mouse_x-self.x))*180/math.pi)
            except:
                pass
                      
            if(angle > 0 and angle < 90):
                self.image = rotate(self.original, angle)
                self.rect = self.image.get_rect() 
                self.y = subusa.rect.centery - (math.sin(angle*(math.pi/180))*80)
            elif(angle < 0 and angle > -90):
                self.image = rotate(self.original, angle)
                self.rect = self.image.get_rect() 
                self.y = subusa.rect.centery
            else:
                mouse_x = subusa.rect.right
            self.x = subusa.rect.right
            self.rect.y = self.y
            self.rect.x = self.x   

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
################################################################

################################################################
class Aimussr():
    def __init__(self, screen, subussr):
        global turn
        global fireussr
        self.image = pygame.image.load('images/aimussr.png')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.y = subussr.rect.centery
        self.x = subussr.rect.left
        self.original = self.image

    def update(self, screen, subussr):
        global angle
        if (turn == 2 and (True!=fireussr)):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #fix stagnant aim
            if (mouse_x > subussr.rect.left - 100):
                mouse_x = subussr.rect.left
                mouse_y = subussr.rect.bottom
            
            rotate = pygame.transform.rotate
            try:
                angle  = (math.tan((self.y-mouse_y)/(mouse_x-self.x))*180/math.pi) - 180
            except:
                pass
            
            if(angle < -180 and angle > -280):
                self.image = rotate(self.original, angle)
                self.y = subussr.rect.centery - (math.sin(angle*(math.pi/180))*80)
                self.x = subussr.rect.left + (math.cos(angle*(math.pi/180))*80)
            elif(angle < -90 and angle > -180):
                self.image = rotate(self.original, angle)
                self.y = subussr.rect.centery
                self.x = subussr.rect.left + (math.cos(angle*(math.pi/180))*80)

            self.rect.y = self.y
            self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
################################################################
class Text():
    def __init__(self, screen):
        pygame.font.init()
        self.screen = screen
        textfont = pygame.font.SysFont('Calibri', 60)
        textsurface = textfont.render('', False, (255,187,76))

    def blitme(self):
        global subusahealth
        global subussrhealth
        textfont = pygame.font.SysFont('Calibri', 60)
        textsurface = textfont.render('', False, (255,187,76))
        if (subusahealth == 0):
            textsurface = textfont.render('THE USSR WINS!!!', False, (255,187,76))
        elif (subussrhealth == 0):
            textsurface = textfont.render('THE USA WINS!!!', False, (255,187,76))

        self.screen.blit(textsurface, (550,150))

################################################################
        



def main():
    pygame.init()
    global ussrsong

# Creating class instances
    ai_settings = Settings()
    
    # Setting the background
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Submarine Sabotage")

    subusa = Subusa(screen)
    subussr = Subussr(screen)
    torpedousa = Torpedousa(screen, subusa, subussr)
    torpedoussr = Torpedoussr(screen, subussr, subusa)
    aimusa = Aimusa(screen, subusa)
    aimussr = Aimussr(screen, subussr)
    background = Background(screen)
    text = Text(screen)
    initialize = True
    if(ussrsong == False):
        pygame.mixer.music.load('sounds/sonar.wav')
    else:
        pygame.mixer.music.load('sounds/ussrsong.wav')
    
    pygame.mixer.music.play()
    playing = True
    
    while playing:
        global turn
        if(initialize):
            global turn
            global subusahealth
            global subussrhealth
            turn = 1
            subusa.update()
            torpedousa.update(screen, subusa, subussr)
            aimusa.update(screen, subusa)
            turn = 2
            subussr.update()
            torpedoussr.update(screen, subussr, subusa)
            aimussr.update(screen, subussr)
            turn = 1
            initialize = False
            
        
        # Watch for keyboard and mouse events
        Game_functions.check_events(subusa, subussr)
        if (turn == 1):
            subusa.update()
            torpedousa.update(screen, subusa, subussr)
            aimusa.update(screen, subusa)
            
            if(subussrhealth <= 0):
                playing = False
                
            #text.update(screen)
        elif (turn == 2):
            subussr.update()
            torpedoussr.update(screen, subussr, subusa)
            aimussr.update(screen, subussr)
            #text.update(screen)
            
            if(subusahealth <= 0):
                playing = False
  
       
        else:
            turn = 1
        
        Game_functions.update_screen(ai_settings, screen, subusa, subussr, torpedousa, torpedoussr, aimusa, aimussr,
                                     background, text)
        if(playing == False):
            time.sleep(5)
            subusahealth = 3
            subussrhealth = 3
################################################################
class title():
    pygame.init()

# Creating class instances
    ai_settings = Settings()
    
    # Setting the background
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    image = pygame.image.load('images/title.png').convert_alpha()
    pygame.display.set_caption("Submarine Sabotage")
    
    

        #stores whether or notuser has pressed enter  
    while True:
        global snek
        global ussrsong
            #watch for keyboard and mouse events
        screen.blit(image, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    #forward or exit
                if event.key == pygame.K_RETURN:
                    main()
                if event.key == pygame.K_u:
                    ussrsong = True
                    print('Mwahahaha, now you must listen to catchy music forever')
                    main()
                    
                if event.key == pygame.K_i:
                    snek = True
                    print('I hope you like parabolas because there is no escaping them now')
                    main()
                    
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    
        
################################################################
title()
