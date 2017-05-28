

import pygame,random,meth_isn  # Python 3.2.4  # Pygame 1.9.2    
from pygame import *   #On importe ce dont on a besoin  
from meth_isn import *
from tkinter import *

window_menu = Tk() # On cree notre fenetre Tkinter pour le menu
window_menu.wm_title("Action Dragon") #On affiche sur l'entete "Action Dragon"

def jeu(): # Fonction du jeu, il est en effet necessaire de definir le jeu en tant que  fonction pour l'incorporer dans le menu Tkinter

	pygame.init() # lancement du jeu
	
	pygame.mixer.init() # Lancement de la musique
	pygame.mixer.music.load("Spirit.wav") # On charge la musique suivant
	pygame.mixer.music.play(-1,0.0) # On lance la musique en boucle a partir du debut

	window = pygame.display.set_mode((1280,640),FULLSCREEN) #1280 = 40*32 #640 = 32*20 # On met en plein ecran
	W = 1280
	H = 640
	niv1_V = pygame.image.load("niv1_V.png")
	niv1_T = pygame.image.load("niv1_T.png")
	niv2_V = pygame.image.load("niv2_V.png")
	niv2_T = pygame.image.load("niv2_T.png")
	niv3_V = pygame.image.load("niv3_V.png")
	niv3_T = pygame.image.load("niv3_T.png")
	img_pause = pygame.image.load("pause.png")
	niveaux=['niv1','niv2','niv3']
	niv = niveau('niveaux',window)
	joueur1=joueur(window,320,320)
	joueur1.affiche()
	pnj_liste = []
	fle_liste = []
	trap_liste = []
	life=50 #On initialise la variable vie des pnj
	sens_fle = "droite" # Sens de la fleche par defaut

	sol = [niv1_V,niv2_V,niv3_V]
	fond = [niv1_T,niv2_T,niv3_T]

	i = random.randint(0,2)
	niveaut=niveaux[i]
	case = sol[i]
	back = fond[i]
	niv.gen_niveau(niveaut)
	niv.affiche_niveau(case,back)

	
	
	pygame.display.flip()
	
	def gen_trap():
 		for i in range(0,5):
 			rand_x = random.randint(30,1260)
 			rand_y = random.randint(30,625)
 			plop = trap(window,rand_x,rand_y)
 			trap_liste.append(plop)
	
	def affiche_trap():
		for pop in trap_liste:
			pop.affiche()
	
	def check_life_col(obj1,obj2):
	
		if pygame.sprite.collide_mask(obj1,obj2):
			obj2.life= obj2.life -25
			atk_time = 0
			


	def check_col_pnj_j(obj1,obj2):
		if pygame.sprite.collide_mask(obj1,obj2):
			obj1.update(-add_x_p,-add_y_p)
			obj2.update(-obj2.add_x,-obj2.add_y)
	def check_col_pnj2(obj1,obj2):
		if pygame.sprite.collide_mask(obj1,obj2):
			obj1.update(-obj1.add_x,-obj1.add_y)
			obj2.update(-obj2.add_x,-obj1.add_y)


	def gen_pnj():
 		for i in range(0,10):
 			rand_x = random.randint(30,1260)
 			rand_y = random.randint(30,625)
 			pn = pnj(window,rand_x,rand_y,life)
 			
 			pnj_liste.append(pn)

	def check_collision(obj): #Verifie si le perso n'est pas en dehors de la fenetre

		if obj.x<0:
			obj.update(32,0)
		if obj.x>=1280:
			obj.update(-32,0)
		if obj.y<0:
			obj.update(0,32)
		if obj.y>=640:
			obj.update(0,-32)
 			
	def affiche_pnj(): #permet le deplacement automatique des pnjs sans sortir de la fenetre
		
		
		for pnj in pnj_liste:
			test = random.randint(0,1) # 0 pour se deplacer horizontalement, 1 pour se deplacer verticalement
			if(test==0):
				if(pnj.x<32):
					pnj.add_x =32
					pnj.add_y =0
					pnj.update(32,0) # Si on est trop proche du bord gauche, on va a droite
				elif(pnj.x>W-32):
					pnj.add_x =-32
					pnj.add_y =0
					pnj.update(-32,0) # Si on est trop proche du bord droit, on va a gauche
				else:
					a = random.randint(-1,1)*32
					pnj.add_x = a
					pnj.add_y =	0
					pnj.update(a,0)# Sinon on fait ce qu'on veut
			else:
				if(pnj.y<32):
					pnj.add_x =0
					pnj.add_y =32
					pnj.update(0,32) # Si on est trop proche du haut, on va en bas
				elif(pnj.y>H-32):
					pnj.add_x =0
					pnj.add_y =-32
					pnj.update(0,-32) # Si on est trop proche du bas, on va en haut
				else:
					a = random.randint(-1,1)*32
					pnj.add_x = 0
					pnj.add_y =	a
					pnj.update(0,a) # Sinon on fait ce qu'on veut
			check_collision(pnj)
			for pou in pnj_liste:
				check_col_pnj2(pou,pnj)
			pnj.affiche()
		

	gen_trap()
	gen_pnj()
	portee = 0 
	atk_time = 0
	continuer = 1
	
	pygame.key.set_repeat(2,50)
	while continuer: 
		pygame.time.Clock().tick(60)
		for event in pygame.event.get():
			add_x_p = 0 # Avance du perso
			add_y_p = 0
			add_x = 0 # Avance des pnj
			add_y = 0
			
			if event.type == QUIT:  #Variable de Pygame
				continuer = 0
				
			if event.type == KEYDOWN:
				
				if event.key == K_ESCAPE:
					continuer=0
					
				if event.key == K_DOWN:
					add_x_p = 0
					add_y_p = 32
					sens_fle ="bas"
				if event.key == K_UP:
					add_x_p = 0
					add_y_p = -32
					sens_fle ="haut"
				if event.key == K_RIGHT:
					add_x_p = 32
					add_y_p = 0
					sens_fle = "droite"
				if event.key == K_LEFT:
					add_x_p = -32
					add_y_p = 0
					sens_fle = "gauche"
				if event.key == K_p: #Pour mettre en pause
					
					continuer_pause = 1
					while continuer_pause:
						pygame.mixer.music.pause()
						window.blit(img_pause,(0,0))
						pygame.display.flip()
						

						for event in pygame.event.get():
							if event.type == QUIT:  #Variable de Pygame
								continuer_pause = 0
								continuer = 0
							if event.type == KEYDOWN:

								
								if event.key == K_p:

									continuer_pause = 0
									pygame.mixer.music.unpause()
					
								if event.key == K_ESCAPE:
									continuer_pause = 0
									continuer=0
								
									
							else:
								pygame.time.wait(50)
								

				if event.key == K_SPACE: 
					atk_time=1	
					pos_f_x = joueur1.x
					pos_f_y = joueur1.y
					fleche = attack(window,pos_f_x,pos_f_y,joueur1,sens_fle,0,1)
					fle_liste.append(fleche)



			joueur1.update(add_x_p,add_y_p)


			check_collision(joueur1)
			
		if atk_time==1:
			for fleche in fle_liste:
				if fleche.sens_fle == "bas":
					fleche.update(0,32)
				if fleche.sens_fle == "haut":
					fleche.update(0,-32)
				if fleche.sens_fle == "droite":
					fleche.update(32,0)
				if fleche.sens_fle == "gauche":
					fleche.update(-32,0)
				fleche.portee = fleche.portee+1
				
				for pnj_o in pnj_liste:
					check_life_col(fleche,pnj_o)
				for pnj_o in pnj_liste:
					if pygame.sprite.collide_mask(pnj_o,fleche):
						fleche.atk_time = 0
						pnj_liste.remove(pnj_o)
						
				if fleche.portee>5:
					fleche.atk_time=0
					fleche.portee = 0
	
		
		for pou in trap_liste:
			check_life_col(pou,joueur1)
		if joueur1.life <=0:
			continuer = 0
		if pnj_liste ==[]:
			continuer=0


		
		for pou in pnj_liste:
				check_col_pnj_j(joueur1,pou)
				for pou2 in pnj_liste:
					check_col_pnj2(pou,pou2)

		niv.affiche_niveau(case,back)
		affiche_trap()
		joueur1.affiche()
		affiche_pnj()
		for fleche in fle_liste:
			fleche.affiche()
		
		pygame.display.flip()
	pygame.quit()




w = window_menu.winfo_screenwidth() #On recupere la largeur et la hauteur de l'ecran
h = window_menu.winfo_screenheight()
window_menu.geometry("%dx%d+0+0" % (w, h)) # Pour localiser ou est la fenetre (Dans notre cas : Plein Ecran)
label = Label(window_menu,text="Menu") #On affiche un Titre
bouton_play =Button(window_menu,height = 10,width = 15 ,text="Play",command=jeu)  # Bouton Play pour lancer le jeu
bouton_quit =Button(window_menu,height = 10,width = 15 ,text="Exit",command=window_menu.quit) # Bouton Exit pour quitter le menu ( et donc le jeu)
label.pack()
bouton_play.grid(row=1,column=1) #On repartis les boutons dans une colonne
bouton_quit.grid(row=2,column=1)
bouton_play.pack()
bouton_quit.pack()
window_menu.mainloop()



                                   

