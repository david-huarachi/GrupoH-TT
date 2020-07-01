import base64
import json
import gzip
import pygame
from pygame.locals import *


class Mapa(object):
    
    _tileH=0
    _tileW=0
    
    _MapaW=0    
    _MapaH=0
   
    _transparentcolor=-1
    _matrizMapa=[]
    _mapaImagenes=[]
    
    _postile=0
    _posfondo=0
    
    _posEnemy=0
    
    _blink_posY=215


    def __init__(self):
        
        
        return
       
       
    def cargarMapa(self,Nivel):
                
        
        f = open("maps/"+Nivel+".json", "r")
        data = json.load(f)
        f.close()
        
        
        i=0
        
        
    
        for item in data["layers"]:            
            self.layers(item)

        for item in data["layers"]:
            self.tilesets(item)
            i+=1
    
            
        
        
        return
       
       
    def layers(self, layer):  
        
        self._MapaW= layer["height"]
        self._MapaH=layer["width"]
        
        matrizTemp=layer["data"]

        self._matrizMapa = [[0] *self._MapaH for i in range(self._MapaW)]

        #Convertir vector en Matriz
        con=0
        for i in range(0,self._MapaW):
            for j in range(0,self._MapaH):
                self._matrizMapa[i][j]=matrizTemp[con]-1
                con=con+1

        
        return
        

       
    def tilesets(self,tileset):

        
        self._tileW=tileset["tilewidth"]
        self._tileH=tileset["tileheight"]        
        
        imgTemp=tileset["image"]
        
        
        self._transparentcolor=tileset["transparentcolor"]
            
        
        img=pygame.image.load("images/"+imgTemp).convert()
        
        if self._transparentcolor!=-1:
            
            alpha=self._transparentcolor        
            alpha = alpha.lstrip('#')
            lv = len(alpha)
            alpha=tuple(int(alpha[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))                            
            img.set_colorkey(alpha, RLEACCEL)
            
            
            
        self.array_Tileset(img)
            
        
        
        return 
       
     
    def array_Tileset(self,img):
        
        
        for i in range(30):

            for j in range(27):
                self._mapaImagenes.append(img.subsurface((j*18,i*18,self._tileW,self._tileH)))
                
                        
        
        for i in range(len(self._mapaImagenes)):
            self._mapaImagenes[i]=pygame.transform.scale2x(self._mapaImagenes[i])
            
        return