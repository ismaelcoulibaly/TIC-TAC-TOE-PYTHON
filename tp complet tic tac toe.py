#ISMAEL COULIBALY           Tic tac toe complet
import random
import pygame
import sys
from sys import exit

pygame.init()

noir = (0, 0 ,0)
blanc = (255, 255, 255)
grisvert =  (0, 255, 0)
rouge = (255, 0, 0)
gris=(128,128,128)

   
Taille =[600, 600]
fenetre = pygame.display.set_mode(Taille)
grille = [['-','-','-'],['-','-','-'],['-','-','-']]
choices = ['X','O']
fenetreGagnant = pygame.display.set_mode(Taille)

def choisirSymbole(choices):# le joueur chosit a partir du menu 
    choixJoueur =''
    
    fenetreMenu = pygame.display.set_mode(Taille)#il s'agit du menu pour que le joueur choisisse le symbole
    symbole_X = pygame.draw.rect(fenetreMenu, gris, (0, 0, 300 ,600))
    symbole_O = pygame.draw.rect(fenetreMenu,noir, (300,0,300,600))

    font = pygame.font.Font('freesansbold.ttf', 32)     
    text = font.render('choisir X', True, noir)
    textRect = text.get_rect()
    textRect.center = (150, 300)
    fenetreMenu.blit(text, textRect)

    text = font.render('choisir O', True, blanc)
    textRect = text.get_rect()
    textRect.center = (450, 300)
    fenetreMenu.blit(text, textRect)


    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                running = False     
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(symbole_X.collidepoint(pos)):
                    choixJoueur = choices[0]
                    running = False
                    return choixJoueur

                elif(symbole_O.collidepoint(pos)):
                    choixJoueur = choices[1]
                    running = False
                    return choixJoueur

        pygame.display.update()           
    
                
def quitterJeu():
    fenetreQuitter = pygame.display.set_mode(Taille)
    rectangle = pygame.draw.rect(fenetreQuitter,noir, (300,600,300,600))

    font = pygame.font.SysFont('arial', 22)
    
    text = font.render('Voulez vous quitter ?', True, blanc)
    textRect = text.get_rect()
    textRect.center = (300, 300)
    fenetreQuitter.blit(text, textRect)

    pygame.display.flip()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                running = False  


    

def drawCross(fenetre,case):# cette fonction dessine une croix
    #case correspond a l'endroit ou on veut faire la croix
    if case == 1:
        pygame.draw.line(fenetre, gris, (35,20), (160,180), 15)
        pygame.draw.line(fenetre, gris, (160,20), (35,180), 15)
        grille[0][0] = 'X'

    elif case == 2:
        pygame.draw.line(fenetre, gris, (200,20), (330,180), 15)
        pygame.draw.line(fenetre, gris, (330,20), (200,180), 15)
        grille[0][1] = 'X'

    elif case == 3:
        pygame.draw.line(fenetre, gris, (370,20), (500,180), 15)
        pygame.draw.line(fenetre, gris, (500,20), (370,180), 15)
        grille[0][2] = 'X'

    elif case == 4:
        pygame.draw.line(fenetre, gris, (35,200), (160,330), 15)
        pygame.draw.line(fenetre, gris, (160,200), (35,330), 15)
        grille[1][0] = 'X'

    elif case == 5:
        pygame.draw.line(fenetre, gris, (200,200), (330,330), 15)
        pygame.draw.line(fenetre, gris, (330,200), (200,330), 15)
        grille[1][1] = 'X'

    elif case ==6:
        pygame.draw.line(fenetre, gris, (370,200), (500,330), 15)
        pygame.draw.line(fenetre, gris, (500,200), (370,330), 15)
        grille[1][2] = 'X'

    elif case ==7:
        pygame.draw.line(fenetre, gris, (35,380), (160,515), 15)
        pygame.draw.line(fenetre, gris, (160,380), (35,515), 15)
        grille[2][0] = 'X'
    elif case ==8:
        pygame.draw.line(fenetre, gris, (200,380), (330,515), 15)
        pygame.draw.line(fenetre, gris, (330,380), (200,515), 15)
        grille[2][1] = 'X'

    elif case == 9:
        pygame.draw.line(fenetre, gris, (370,380), (500,515), 15)
        pygame.draw.line(fenetre, gris, (500,380), (370,515), 15)
        grille[2][2] = 'X'

    pygame.display.flip()


###########generalisation du jeu
fenetreGeneralisation = pygame.display.set_mode(Taille)
rectangle = pygame.draw.rect(fenetreGeneralisation,rouge, (300,600,300,600))
font = pygame.font.Font(pygame.font.get_default_font(), 32)     
text = font.render('Combien de colonnes et de lignes voulez-vous ? ', True, noir)
textRect = text.get_rect()
textRect.center = (150, 300)
fenetreGeneralisation.blit(text, textRect)

pygame.display.flip()
nbRec = int(input("Combien de colonnes et de lignes voulez-vous ?"))
positionRectangle=[25,25,150,150]
for i in range(0,nbRec):
    for y in range (0,nbRec):
        rec = pygame.draw.rect(fenetre,blanc,positionRectangle)
        positionRectangle[1] = 175 +positionRectangle[1] 
    positionRectangle[1] =25
    positionRectangle[0] = 175 + positionRectangle[0] 

choisirSymbole(choices)
choixJoueur = choisirSymbole(choices)
pygame.display.flip()


###########generalisation du jeu


#gagnant

pygame.display.flip()

pygame.display.set_caption("bienvenue!")



#boucle jusqu'à ce que l'utilisateur décide de fermer la fenêtre
termine = False
rect_circle_switch = True
case1_disponible = True
case2_disponible = True
case3_disponible = True
case4_disponible = True
case5_disponible = True
case6_disponible = True
case7_disponible = True
case8_disponible = True
case9_disponible = True

cases = [[case1_disponible, case2_disponible,case3_disponible],
[case4_disponible,case5_disponible,case6_disponible], 
[case7_disponible,case8_disponible,case9_disponible]]


#à quelle vitesse l'écran met à jour
# vitesse de jeu,
#attention a C de Clock
horloge = pygame.time.Clock()


(X1,Y1) = (100,100)
(X2,Y2) = (275,100)
(X3,Y3) = (450,100)

(X4,Y4) = (100,275)
(X5,Y5) = (275,275)
(X6,Y6) = (450,275)

(X7,Y7) = (100,450)
(X8,Y8) = (275,450)
(X9,Y9) =(450,450)

coordonneesCases = [(X1,Y1),(X2,Y2),(X3,Y3),
(X4,Y4), (X5,Y5),(X6,Y6),
(X7,Y7),(X8,Y8),(X9,Y9)]

def gagnant(grille):
    
    rectangle = pygame.draw.rect(fenetreGagnant,noir, (300,600,300,600))
    font = pygame.font.SysFont('arial', 22)


    #on verifie par ligne
    for ligne in grille:
        
        if ligne[0] == ligne[1] and ligne[0] == ligne[2] and ligne[1] == ligne[2] and ligne[0] != '-' and ligne[0] == choixJoueur:
            text = font.render('Le joueur a gagne', True, gris)
            textRect = text.get_rect()
            textRect.center = (150, 300)
            fenetreGagnant.blit(text, textRect)

        if ligne[0] == ligne[1] and ligne[0] == ligne[2] and ligne[1] == ligne[2] and ligne[0] != '-' and ligne[0] != choixJoueur:
            text = font.render('L\'ordinateur a gagne', True, gris)
            textRect = text.get_rect()
            textRect.center = (150, 300)
            fenetreGagnant.blit(text, textRect)
    

    #on verifie par colonne
    for col in range(len(grille)):
        uneListe = []
    
        if(ligne[0] != '-'):    
            for ligne in grille:
                uneListe.append(ligne[0])

    if ligne[0] != '-' and uneListe.count(uneListe[0]) == len(uneListe) and uneListe[0] == choixJoueur:
        text = font.render('Vous avez gagne', True, gris)
        textRect = text.get_rect()
        textRect.center = (150, 300)
        fenetreGagnant.blit(text, textRect)

    if ligne[0] != '-' and uneListe.count(uneListe[0]) == len(uneListe) and uneListe[0] != choixJoueur:
        text = font.render("l'\ordinateur a gagne", True, gris)
        textRect = text.get_rect()
        textRect.center = (150, 300)
        fenetreGagnant.blit(text, textRect)


    #on verifie pour les diagonales
    diag_1 =[]
    for i in range(len(grille)):
        if grille[i][i] != '-':
            diag_1.append(grille[i][i])
    if grille[i][i] != '-' and diag_1.count(diag_1[0]) == 3 and diag_1[0] != choixJoueur:
        text = font.render("l'\ordinateur a gagne", True, gris)
        textRect = text.get_rect()
        textRect.center = (150, 300)
        fenetreGagnant.blit(text, textRect)

    if grille[i][i] != '-' and diag_1.count(diag_1[0]) ==3 and diag_1[0] == choixJoueur:
        text = font.render('Vous avez gagne', True, gris)
        textRect = text.get_rect()
        textRect.center = (150, 300)
        fenetreGagnant.blit(text, textRect)

    diag_2 =[]
    for col,ligne in enumerate(reversed(range(len(grille)))):
        if(grille[ligne][col]!='-'):
            diag_2.append(grille[ligne][col])
    


    if grille[ligne][col]!='-' and diag_2.count(diag_2[0]) == 3 and diag_2[0] != choixJoueur:
        text = font.render("l'\ordinateur a gagne", True, gris)
        textRect = text.get_rect()
        textRect.center = (150, 300)
        fenetreGagnant.blit(text, textRect)

    if grille[ligne][col]!='-' and diag_2.count(diag_2[0]) == 3 and diag_2[0] == choixJoueur:
        text = font.render("Vous avez gagne", True, gris)
        textRect = text.get_rect()
        textRect.center = (150, 300)
        fenetreGagnant.blit(text, textRect)


while termine == False:

    nbTour =1
    #event comme clic de souris 
    #pygame.event.get() est un list
    clicked = False
    while clicked == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #true monte whie met termine = True, et attend pour 20 second 
                termine = True

            #quitterJeu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    termine =False  
                    pygame.display.quit()
                    sys.exit(0)

                    
                
        #LOGIQUE CEST ICI

        #icc il s'agit du code concernant le joeur vu qu'il est le seul a utiliser la souris
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
            
                if rec_1.collidepoint(pos) and case1_disponible:
                    if choixJoueur == 'X' :
                        drawCross(fenetre,1)
                        
                        
                        rect_circle_switch = False
                    else:
                        # (100,100) le centre du circle, 50 rayon )        
                        pygame.draw.circle(fenetre, gris, (X1,Y1), 50,18)
                        grille[0][0] = 'O'
                        rect_circle_switch = True
                    case1_disponible = False 
                    clicked = True 
                
                if rec_2.collidepoint(pos) and case2_disponible:
                    if choixJoueur == 'X' :
                        drawCross(fenetre,2)
                        rect_circle_switch = False
                    else:
                        # on ajoute 100 + 175 =275
                        pygame.draw.circle(fenetre, gris, (X2,Y2), 50, 18)
                        grille[0][1] = 'O'
                        rect_circle_switch = True
                    
                    case2_disponible = False
                    clicked = True
                
                if rec_3.collidepoint(pos) and case3_disponible :
                    if choixJoueur == 'X' :
                        drawCross(fenetre,3)
                        rect_circle_switch = False
                    else:

                        pygame.draw.circle(fenetre, gris, (X3,Y3), 50, 18)
                        grille[0][2] = 'O'
                        rect_circle_switch = True
                    case3_disponible = False
                    clicked = True
                        
                if rec_4.collidepoint(pos) and case4_disponible :
                    if choixJoueur == 'X' :
                        drawCross(fenetre,4)
                        rect_circle_switch = False
                    else:
                        pygame.draw.circle(fenetre, gris, (X4,Y4), 50, 18)
                        grille[1][0] = 'O'
                        rect_circle_switch = True
                    
                    case4_disponible = False
                    clicked = True
                    
                if rec_5.collidepoint(pos) and case5_disponible:
                    if choixJoueur == 'X' :
                        drawCross(fenetre,5)
                        rect_circle_switch = False
                    else:
                        pygame.draw.circle(fenetre, gris, (X5,Y5), 50, 18)
                        grille[1][1] = 'O'
                        rect_circle_switch = True
                    
                    case5_disponible = False
                    clicked = True
                
                if rec_6.collidepoint(pos) and case6_disponible:
                    if choixJoueur == 'X' :
                        drawCross(fenetre,6)
                        rect_circle_switch = False
                    else:
                        pygame.draw.circle(fenetre, gris, (X6,Y6), 50, 18)
                        grille[1][2] = 'O'
                        rect_circle_switch = True
                    
                    case6_disponible = False
                    clicked = True
                    
                if rec_7.collidepoint(pos) and case7_disponible:
                    if choixJoueur == 'X' :
                        drawCross(fenetre,7)
                        rect_circle_switch = False
                    else:
                        pygame.draw.circle(fenetre, gris, (X7,Y7), 50, 18)
                        grille[2][0] = 'O'
                        rect_circle_switch = True
                    
                    case7_disponible = False
                    clicked = True
                
                if rec_8.collidepoint(pos) and case8_disponible:
                    if choixJoueur == 'X' :
                        drawCross(fenetre,8)
                        rect_circle_switch = False
                    else:
                        pygame.draw.circle(fenetre, gris, (X8,Y8), 50, 18)
                        grille[2][1] = 'O'
                        rect_circle_switch = True
                    
                    case8_disponible = False
                    clicked = True
                    
                if rec_9.collidepoint(pos) and case9_disponible:
                    if choixJoueur == 'X' :
                        drawCross(fenetre,9)
                        rect_circle_switch = False
                    else:
                        pygame.draw.circle(fenetre, gris,  (X9,Y9), 50, 18)
                        grille[2][2] = 'O'
                        rect_circle_switch = True
                    case9_disponible = False
                    clicked = True
                
    caseDisponible = False
    randomIndex1 = ''
    randomIndex2 = ''
    while caseDisponible ==False:
        randomIndex1 = random.randrange(len(grille))
        randomIndex2 = random.randrange(len(grille[randomIndex1]))
        randomCase = grille[randomIndex1][randomIndex2]
        if randomCase == '-' :caseDisponible = True
        if(case1_disponible == False  and case2_disponible == False and case3_disponible == False
    and case4_disponible == False and case5_disponible == False  and case6_disponible == False 
    and case7_disponible == False and case8_disponible == False and case9_disponible == False):
            caseDisponible = True

    if grille[randomIndex1][randomIndex2] == '-' and choixJoueur =='X':
        if( (randomIndex1, randomIndex2) == (0,0)):
            grille[randomIndex1][randomIndex2] = 'O'
            pygame.draw.circle(fenetre, gris,(X1,Y1) ,50,18)
            case1_disponible = False

        if((randomIndex1, randomIndex2) == (0,1)):
            grille[randomIndex1][randomIndex2] = 'O'
            pygame.draw.circle(fenetre, gris,(X2,Y2) ,50,18)
            case2_disponible = False

        if((randomIndex1, randomIndex2) == (0,2)):
            grille[randomIndex1][randomIndex2] = 'O'
            pygame.draw.circle(fenetre, gris,(X3,Y3) ,50,18)
            case3_disponible = False


        if((randomIndex1, randomIndex2) == (1,0)):
            grille[randomIndex1][randomIndex2] = 'O'
            pygame.draw.circle(fenetre, gris,(X4,Y4) ,50,18)
            case4_disponible = False

        if((randomIndex1, randomIndex2) == (1,1)):
            grille[randomIndex1][randomIndex2] = 'O'
            pygame.draw.circle(fenetre, gris,(X5,Y5) ,50,18)
            case5_disponible = False

        if((randomIndex1, randomIndex2) == (1,2)):
            grille[randomIndex1][randomIndex2] = 'O'
            pygame.draw.circle(fenetre, gris,(X6,Y6) ,50,18)
            case6_disponible = False

        if((randomIndex1, randomIndex2) == (2,0)):
            grille[randomIndex1][randomIndex2] = 'O'
            pygame.draw.circle(fenetre, gris,(X7,Y7) ,50,18)
            case7_disponible = False

        if((randomIndex1, randomIndex2) == (2,1)):
            grille[randomIndex1][randomIndex2] = 'O'
            pygame.draw.circle(fenetre, gris,(X8,Y8) ,50,18)
            case8_disponible = False

        if((randomIndex1, randomIndex2) == (2,2)):
            grille[randomIndex1][randomIndex2] = 'O'
            pygame.draw.circle(fenetre, gris,(X9,Y9) ,50,18)
            case9_disponible = False

#si le joueur choisit O alors l'ordinateur aura X
    elif grille[randomIndex1][randomIndex2] == '-' and choixJoueur =='O':
        if( (randomIndex1, randomIndex2) == (0,0)):
            grille[randomIndex1][randomIndex2] = 'X'
            drawCross(fenetre,1)

        if((randomIndex1, randomIndex2) == (0,1)):
            grille[randomIndex1][randomIndex2] = 'X'
            drawCross(fenetre,2)

        if((randomIndex1, randomIndex2) == (0,2)):
            grille[randomIndex1][randomIndex2] = 'X'
            drawCross(fenetre,3)


        if((randomIndex1, randomIndex2) == (1,0)):
            grille[randomIndex1][randomIndex2] = 'X'
            drawCross(fenetre,4)

        if((randomIndex1, randomIndex2) == (1,1)):
            grille[randomIndex1][randomIndex2] = 'X'
            drawCross(fenetre,5)

        if((randomIndex1, randomIndex2) == (1,2)):
            grille[randomIndex1][randomIndex2] = 'X'
            drawCross(fenetre,6)

        if((randomIndex1, randomIndex2) == (2,0)):
            grille[randomIndex1][randomIndex2] = 'X'
            drawCross(fenetre,7)

        if((randomIndex1, randomIndex2) == (2,1)):
            grille[randomIndex1][randomIndex2] = 'X'
            drawCross(fenetre,8)

        if((randomIndex1, randomIndex2) == (2,2)):
            grille[randomIndex1][randomIndex2] = 'X'
            drawCross(fenetre,9)
    
    ###on verifie a chaque iteration qui est le gagnant
    gagnant(grille)
    pygame.display.flip()   

  
    # si on dessin le rectangle ici, on voit rien
    
    #20 images par seconde, 10 moin vite que 20        
    horloge.tick(20)
    if(case1_disponible == False  and case2_disponible == False and case3_disponible == False
    and case4_disponible == False and case5_disponible == False  and case6_disponible == False 
    and case7_disponible == False and case8_disponible == False and case9_disponible == False):
        termine = True
        fenetre.blit(pygame.Surface(Taille),(0,0))
        quitterJeu()
        
pygame.display.flip()

quitterJeu()

#quitterJeu()


    

        





    
