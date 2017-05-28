import pygame,math         #On importe ce dont on a besoin     
from pygame import *
from math import *

class niveau(): # Classe du niveau
	def __init__(self,niveau,screen): #Methode init niveau
		self.niveau = niveau   #Nom du fichier texte qui contient le niveau
		self.screen = screen #Nom de la fenêtre où il sera affiché
		self.structure_niveau = 0
		


	def gen_niveau(self,niveau): #Methode pour generer le niveau et sa structure
		
		with open(niveau, "r") as niveau:
			structure =[]
			for ligne in niveau:
				
				lettre_ligne=[]
		
				for lettre in ligne:
			
					if lettre != '\n':
						lettre_ligne.append(lettre)

				structure.append(ligne)
			self.structure_niveau = structure
		

	def affiche_niveau(self,V,T): #Methode pour afficher le niveau
		self.V = V
		self.T = T
		img_y = 0
		for ligne in self.structure_niveau:
			img_x =0
			for lettre in ligne:

				if lettre =="V":
					self.screen.blit(V,(img_x,img_y))
				if lettre =="T":
					self.screen.blit(T,(img_x,img_y))
				
				img_x = img_x+32
			img_y = img_y+32
	


		
class joueur(pygame.sprite.Sprite):   # Classe du du joueur
	                          				
	def __init__(self,screen,x,y):# methode principale du perso
		self.image = pygame.image.load('draconian_green_m.png')# image
		self.screen = screen #Nom de la fenêtre où il sera affiché
		self.x = x  # position x
		self.y = y # position y
		self.life = 100
		self.rect = self.image.get_rect()                   # rect = celui img
		self.image_w, self.image_h = self.image.get_size()  # taille = celle img
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)         # en haut a gauche
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h) # en  bas a droite
		self.mask = pygame.mask.from_surface(self.image) #Mask lie au sprite                      
	def affiche(self):
		if self.life>0:
			self.screen.blit(self.image,(self.x,self.y))              #Permet d'afficher l'image
	
	def update(self,add_x,add_y):
		self.x = self.x + add_x    # Notre img bouge
		self.y = self.y + add_y
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)     # Notre rect.rectangle aussi
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)  
	
class attack(pygame.sprite.Sprite): #Class de l'attaque
	def __init__(self,screen,x,y,lanceur,sens_fle,portee,atk_time):
		self.image = pygame.image.load('arrow2.png')
		self.screen = screen #Nom de la fenêtre où il sera affiché
		self.x = x
		self.y = y
		self.sens_fle = sens_fle
		self.portee = portee
		self.atk_time = atk_time
		self.lanceur = lanceur
		self.rect = self.image.get_rect()
		self.image_w,self.image_h = self.image.get_size()
		self.rect.move(self.x,self.y)
		self.rect.topleft = (self.x,self.y)
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
		self.mask = pygame.mask.from_surface(self.image)
		if sens_fle =="haut":
			self.image = fleche_haut
		if sens_fle =="bas":
			self.image= fleche_bas
		if sens_fle == "droite":
			self.image = fleche_droite
		if sens_fle == "gauche":
			self.image = fleche_gauche
	def affiche(self):
		if self.atk_time ==1:
			self.screen.blit(self.image,(self.x,self.y))
	def update(self,add_x,add_y):
		self.x = self.x + add_x    # Notre img bouge
		self.y = self.y + add_y
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)     # Notre rect aussi
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h) 
		self.mask = pygame.mask.from_surface(self.image) 
	
class trap(pygame.sprite.Sprite):  #Classe du piège
	def __init__(self,screen,x,y):
		self.image = pygame.image.load('trap.png')
		self.screen =screen #Nom de la fenêtre où il sera affiché
		self.x = x
		self.y = y
		self.rect = self.image.get_rect()                   # rect = celui img
		self.image_w, self.image_h = self.image.get_size()  # taille = celle img
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)         # en haut a gauche
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h) # en  bas a droite
		
		self.mask = pygame.mask.from_surface(self.image)
	def affiche(self):
		self.screen.blit(self.image,(self.x,self.y))


class pnj(pygame.sprite.Sprite):   # Classe du pnj
	                        
    				
	def __init__(self,screen,x,y,life):# methode principale du perso
		self.image = pygame.image.load('draconian_purple_f.png')# image
		self.screen = screen #Nom de la fenêtre où il sera affiché
		self.x = x  # position x
		self.y = y # position y
		self.add_x = 0
		self.add_y = 0
		self.life = life
		self.rect = self.image.get_rect()                   # rect = celui img
		self.image_w, self.image_h = self.image.get_size()  # taille = celle img
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)         # en haut a gauche
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h) # en  bas a droite
		self.mask = pygame.mask.from_surface(self.image) #Mask lie au sprite                      
	def affiche(self):
		if self.life>0:
			self.screen.blit(self.image,(self.x,self.y))#Permet d'afficher l'image

	
	def update(self,add_x,add_y):
		self.add_x = add_x
		self.add_y = add_y
		self.x = self.x + add_x    # Notre img bouge
		self.y = self.y + add_y
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)     # Notre rect.rectangle aussi
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)  
		self.mask = pygame.mask.from_surface(self.image)
	
	

fleche_droite = pygame.image.load("arrow2.png")
fleche_gauche = pygame.transform.rotate(fleche_droite,180)
fleche_haut = pygame.transform.rotate(fleche_droite,90)           # Differentes img de la fleche avec des angles differents
fleche_bas = pygame.transform.rotate(fleche_droite,270)


