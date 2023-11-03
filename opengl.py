import pygame
import glm
import math
from pygame.locals import *
from Render import Render
from modelo import modelo
from Shaders import *
from objeto import Objt

width = 1080
height = 600
pygame.init()
pantalla = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
Render = Render(pantalla)
vertsha = vrshad
fragsha = frshad
Render.shaders(vertsha, fragsha)
obi = Objt("modelos/gato.obj").datan()
mdlo = modelo(obi)
mdlo.crgartxtu("textura/gato.bmp")
mdlo.pos.z = -15
mdlo.pos.y = -10
mdlo.rttn.x = 270
mdlo.tama = glm.vec3(0.2, 0.2, 0.2)
Md = {"mdlo": mdlo,"Lint": 5.0,"hint": 0.3,"ver": glm.vec3(mdlo.pos.x, mdlo.pos.y + 2 , mdlo.pos.z),"dluz": glm.vec3(0, 0, -1)}
Render.escena.append(Md['mdlo'])
Render.Lint = Md['Lint']
Render.hint = Md['hint']
Render.obje = Md['ver']
Render.dluz = Md['dluz']
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    Render.cambvmat()
    Render.renderizar()
    pygame.display.flip()
