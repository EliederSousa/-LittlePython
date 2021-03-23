import pygame
from pygame.locals import *
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
azul = pygame.Color("blue")
preto = pygame.Color("black")
fonte = pygame.font.SysFont("Consolas", 14)

gravidade = .00009
pontuacao = 0

class Vec2():
	def __init__(self, x, y):
		if y == "angle":
			self.x = math.cos(_PI180 * x)
			self.y = math.sin(_PI180 * x)
		else:
			self.x = x
			self.y = y
	
	def clone(self):
		return Vec2(self.x, self.y)
	
	def add(self, point ):
		self.x += point.x
		self.y += point.y

	def sub(self, point ):
		self.x -= point.x
		self.y -= point.y
		
	def mul(self, point ):
		self.x *= point.x
		self.y *= point.y
	
	def div(self, point ):
		self.x /= point.x
		self.y /= point.y 
	
	def normalize(self):
		return Vec2(self.x / self.size(), self.y / self.size() )
	
	def size(self):
		return math.sqrt( (self.x * self.x) + (self.y * self.y) ) 
	
	def scale(self, factor ):
		self.x *= factor
		self.y *= factor
	
	def limit(self, maximum ):
		if self.size() > maximum:
			normalized = normalize()
			normalized.scale( maximum )
			self.x = normalized.x
			self.y = normalized.y
	
	def getAngle(self):
		return ((180 / math.pi) * math.atan2(self.y, self.x))

class Bola:
    def __init__(self, x, y, radius):
        self.position = Vec2(x, y)
        self.velocity = Vec2(0, 0)
        self.acceleration = Vec2(0, 0)
        self.radius = radius
        self.radiusSquared = radius**2
        
    
class Mouse:
    def __init__(self):
        self.position = Vec2(0, 0)
        
    def setPosition(self, x, y):
        self.position = Vec2(x, y)
    
def circlePointCollision( circle, point ):
    # Calcula a distância entre o círculo e o ponto
    dist = ((point.position.x - circle.position.x)**2) + ((point.position.y - circle.position.y)**2)
    if dist < circle.radiusSquared:
        return True
    else:
        return False


objetos = []
for w in range(4):
    objetos.append(Bola((w*200)+100, 100, 20))

mouse = Mouse()
paused = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == MOUSEMOTION:
            mouse.setPosition( pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] )
            
    if not paused:
    
        screen.fill(pygame.Color("white"))
        
        # Física. =)
        for w in objetos:
            bola = w
            
            # Integração de Euler. 
            bola.velocity.add( Vec2( 0, gravidade ) )
            bola.position.add( bola.velocity )
            
            pygame.draw.circle(screen, azul, (bola.position.x, bola.position.y), bola.radius, 1)
            if circlePointCollision( bola, mouse ):
                bola.velocity.scale( -1 )
            
            if bola.position.y > 800:
                text = fonte.render("VOCÊ PERDEU! Pontuação: {0}".format( int(pontuacao) ), True, preto)
                textPosition = text.get_rect()
                textPosition.topleft = (250, 200)
                screen.blit(text, textPosition)
                paused = True
        
        pygame.draw.circle(screen, pygame.Color("red"), (mouse.position.x, mouse.position.y), 3, 3)
        text = fonte.render("Pontuação: {0}".format( int(pontuacao) ), True, preto)
        textPosition = text.get_rect()
        textPosition.topleft = (300, 10)
        screen.blit(text, textPosition)
        pontuacao += .001
        gravidade += 0.000000005
        
        pygame.display.update()