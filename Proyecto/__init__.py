#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame


import os

import Util 
import Personajes
import Escenario

 
#Tamaño  la pantalla
WIDTH = 32*30
HEIGHT = 32*15

blink=True
cont_blink=0


def Initialize():
    
    global clock, screen, nivel
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Super Jueguito")
    clock = pygame.time.Clock()
    
    
    
   
    return screen
 
def LoadContent():
    
    global personaje1, nivel,fondo, enemigos,over,mano
     
    personaje1 = Personajes.personaje1()
    
    nivel= Escenario.Mapa()
    
    nivel.cargarMapa("Nivel1")
    
    fondo = Util.imagen("images/clouds.png", False, True)
   
    over = Util.imagen("images/over.png", True, True)
   
    mano= over.subsurface((1,1,24,18))
    
    over = over.subsurface((12,48,512,446))
    
    
   
    enemigos=[]
    
    enemigos.append(Personajes.Enemy("goomba",250,True))    
    enemigos.append(Personajes.Enemy("koopa",1500,True))
    enemigos.append(Personajes.Enemy("goomba",1800))    
    enemigos.append(Personajes.Enemy("koopa",2000))
    enemigos.append(Personajes.Enemy("goomba",2100))   
    enemigos.append(Personajes.Enemy("koopa",2500))

    
     
    #sonido = pygame.mixer.Sound("leon.mp3")


    return

def Updates():

    global personaje1
   
    Util.teclado(personaje1,nivel, WIDTH)
    
    
    if Util.colision(personaje1, enemigos)==True:
        
        #solamente archivos WAV y OGG sin comprimir
        sonido= pygame.mixer.Sound("audio/pum.wav")
        sonido.play();
        
   
    return
 
 


def Draw():
    global time, nivel, cont_blink,blink
     
    #Escenario y fondo
    nivel._posfondo-=0.3
    
    screen.blit(fondo, (nivel._posfondo, 0))

    
    for i in range(0,nivel._MapaW):
        for j in range(0,nivel._MapaH):           
            pos=nivel._matrizMapa[i][j]
            screen.blit(nivel._mapaImagenes[pos],(j*32+nivel._postile,i*32) )
    
        
   
    #Dibujar Personaje1
   
    if personaje1._vida==True:
        if personaje1._salto==False:
            
            if personaje1._direc==True:
                screen.blit(personaje1.imagenMario(),(personaje1._posX,mario._posY))
            else:
                personaje1_inv=pygame.transform.flip(personaje1.imagenpersonaje1(),True,False);
                screen.blit(personaje1_inv,(personaje1._posX,personaje1._posY))
        else :        
            personaje1.saltar()
            if personaje1._direc==True:
                screen.blit(personaje1._images[3],(personaje1._posX,personaje1._posY))
            else:
                personaje1_inv=pygame.transform.flip(personaje1._images[3],True,False);
                screen.blit(personaje1_inv,(personaje1._posX,personaje1._posY))
        #Dibujar Enemigos
        
        for enemy in enemigos:
               
            if enemy._activo==True:   
                screen.blit(enemy.animacion(personaje1,WIDTH),(enemy._posX,enemy._posY))
            else:
                if mario._posAbs<=enemy._posX-500:
                    enemy._activo=True
       
    #Muerte de personaje1
    else:
        screen.blit(personaje1.muerteMario(),(personaje1._posX,personaje1._posY))
            
        if personaje1._posY>=480:
            
            
            cont_blink=cont_blink+1
            screen.fill(0)
            screen.blit(over,(190,10))
            
            if cont_blink%20==0:
                blink=not blink
            
            if blink==True:    
                screen.blit(mano,(325,nivel._blink_posY))
                
    
    
    
    pygame.display.flip()
   
    return
 
 
 
 
def main():
   
    Initialize()
   
    LoadContent()

    #pygame.mixer.music.load("audio/fondo.mp3")
    #pygame.mixer.music.play(-1)
     
    
    
    while True:
       
        time = clock.tick(69)
       
        
        Updates()
       
        Draw()
       
       
       
        #if gameOver==True
        #    pygame.mixer.music.stop()
         
     
   
    return
 
 
 
 
if __name__ == '__main__':
    main()
    