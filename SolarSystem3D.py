# -*- coding: utf-8 -*-

from vpython import *


###############################################################################
# Constantes
###############################################################################

G = 6.67e-11            # constante gravitationnelle
UA = 1.496e11           # valeur de l'unité astronimique en m
J = 24*3600             # une journée en secondes
L = 2*UA                # Longueur des axes fixes de l'esapce




###############################################################################
# Critères à changer
###############################################################################


# Choix de la fraction de journée : le pas sera de 1/n jours
#n = 50 ou n = 30 pour les planetes proches
#n = 1/2 ou 1/10 pour les planetes distantes)

n = 30
dt = J/n    # (NE PAS CHANGER) dt est en seconde, il vaut l'équivalent d'une journée divisée par n


nb_boucles = 10000      # Nombre d'itérations par seconde


t0 = 500                 # Date de début des secondes mesures (en jours)



# Paramètres de la fenetre d'affichage :

scene.width = 1600
scene.height = 800






###############################################################################
# Augmentation de la taille des rayons des planètes
###############################################################################

K = 3e1             # coef général

K_Soleil = 4e-1
K_Mercure = 3e1
K_Venus = 3e1
K_Terre = 3e1
K_Mars = 3e1
K_Jupiter = 5
K_Saturne = 5
K_Neptune = 1e1
K_Uranus = 1e1

K_Comete = 2e1



###############################################################################
# Repère du système
###############################################################################

xaxis = curve(color=color.gray(0.5), radius=3e8)
xaxis.append(vec(0,0,0))
xaxis.append(vec(L,0,0))
yaxis = curve(color=color.gray(0.5), radius=3e8)
yaxis.append(vec(0,0,0))
yaxis.append(vec(0,L,0))
zaxis = curve(color=color.gray(0.5), radius=3e8)
zaxis.append(vec(0,0,0))
zaxis.append(vec(0,0,L))

#Lumière du soleil (lumière locale)
sunlight = local_light( pos = vec(0,0,0) , color=color.white )


###############################################################################
# Conditions initiales des planetes/comètes
###############################################################################

p_Soleil = vec(0,0,0)
v_Soleil = vec(0,0,0)

p_Mercure = vec(-0.3605235389982*UA,-0.2295196524382*UA,-0.0852315336377*UA)
v_Mercure = vec(0.0100192527809*UA/J,-0.0191400552251*UA/J,-0.0112630546274*UA/J)

p_Venus = vec(-0.1419512801355*UA,0.6394744400220*UA,0.2967053702075*UA)
v_Venus = vec(-0.0198960915090*UA/J,-0.0042011046637*UA/J,-0.0006313571786*UA/J)

p_Terre = vec(0.6660194257251*UA,0.6724379486446*UA,0.2915034947287*UA)
v_Terre = vec(-0.0130168592984*UA/J,0.0105619744713*UA/J,0.0045782584319*UA/J)

p_Mars = vec(-1.4650308129825*UA,0.7044056556057*UA,0.3626419411604*UA)
v_Mars = vec(-0.0061198215136*UA/J,-0.0101705306722*UA/J,-0.0044997548366*UA/J)

p_Jupiter = vec(-5.0449455542874*UA,1.7365335799939*UA,0.8671469995973*UA)
v_Jupiter = vec(-0.0027987878021*UA/J,-0.0061778163059*UA/J,-0.0025798526529*UA/J)

p_Saturne = vec(-3.9630186778637*UA,-8.5486870936750*UA,-3.3604354836320*UA)
v_Saturne = vec(0.0048158336978*UA/J,-0.0019878598256*UA/J,-0.0010285673888*UA/J)

p_Uranus = vec(18.9351540880573*UA,5.9345078714020*UA,2.3314725062003*UA)
v_Uranus = vec(-0.0012845554949*UA/J,0.0032338724126*UA/J,0.0014345703053*UA/J)

p_Neptune = vec(27.8936389075488*UA,-9.8602445308460*UA,-4.7302409288550*UA)
v_Neptune = vec(0.0011226149958*UA/J,0.0027270583071*UA/J,0.0010881130665*UA/J)



p_Comete_Halley = vec(-33.644*UA,0,10.784*UA)
v_Comete_Halley = vec(-0.00033896232*UA/J,-0*UA/J,-0.00033896232*UA/J)
axe_comete_Halley = p_Comete_Halley

p_Comete_Tempel = vec(-3.873*UA,0,2.746*UA)
v_Comete_Tempel = vec(-0.00389*UA/J,-0,-0.00389*UA/J) 
axe_comete_Tempel = p_Comete_Halley

p_Comete_Tchouri = vec(4.583*UA,0,-3.360*UA)
v_Comete_Tchouri = vec(-0.003048*UA/J,-0,-0.003048*UA/J)
axe_comete_Tchouri =  p_Comete_Tchouri


###############################################################################
# Définition du dystème solaire
###############################################################################

# Activation des trajectoires (vrai ou faux)
Trail = True


"""     # Version couleurs basiques et sans les comètes
Soleil = sphere(pos = vec(0,0,0) , vit = vec(0,0,0) , radius = 1392e6*K*K_Soleil , masse = 2e30 , color = color.orange , pos_init = p_Soleil)
Mercure = sphere(pos = p_Mercure , vit = v_Mercure , radius = 4878e3*K*K_Mercure , masse = 330e21 , color = color.yellow , make_trail = Trail , pos_init = p_Mercure , periode_theo = 87.97)
Venus = sphere(pos = p_Venus , vit = v_Venus , radius = 12104e3*K*K_Venus , masse = 4871e21 , color = color.yellow , make_trail = Trail , pos_init = p_Venus , periode_theo = 224.70)
Terre = sphere(pos = p_Terre , vit = v_Terre , radius = 12756e3*K*K_Terre , masse = 5974e21 , color = color.blue , make_trail = Trail , pos_init = p_Terre , periode_theo = 365.26)
Mars = sphere(pos = p_Mars , vit = v_Mars , radius = 6794e3*K*K_Mars , masse = 641e21 , color = color.red , make_trail = Trail , pos_init = p_Mars , periode_theo = 686.98)
Jupiter = sphere(pos = p_Jupiter , vit = v_Jupiter , radius = 142800e3*K*K_Jupiter , masse = 1899000e21 , color = color.orange , make_trail = Trail , pos_init = p_Jupiter , periode_theo = 4332.7)
Saturne = sphere(pos = p_Saturne , vit = v_Saturne , radius = 120000e3*K*K_Saturne , masse = 568000e21 , color = color.yellow , make_trail = Trail , pos_init = p_Saturne , periode_theo = 10759.5)
Uranus = sphere(pos = p_Uranus , vit = v_Uranus , radius = 51120e3*K*K_Uranus , masse = 86760e21 , color = color.blue , make_trail = Trail , pos_init = p_Uranus , periode_theo = 30685)
Neptune = sphere(pos = p_Neptune , vit = v_Neptune , radius = 49528e3*K*K_Neptune , masse = 103000e21 , color = color.blue , make_trail = Trail , pos_init = p_Neptune , periode_theo = 60190)

"""


        #Version avec les textures des planetes + comètes
        
Soleil = sphere(name = 'Soleil' , pos = vec(0,0,0) , vit = vec(0,0,0) , radius = 1392e6*K*K_Soleil , masse = 2e30 , texture = "http://i.imgur.com/yoEzbtg.jpg" , pos_init = p_Soleil)
Mercure = sphere(name = 'Mercure' , pos = p_Mercure , vit = v_Mercure , radius = 4878e3*K*K_Mercure , masse = 330e21 , texture ='https://media.gettyimages.com/illustrations/mercury-artwork-illustration-id460715395' , make_trail = Trail , pos_init = p_Mercure , periode_theo = 87.97, periode_t0=0)
Venus = sphere(name = 'Venus' , pos = p_Venus , vit = v_Venus , radius = 12104e3*K*K_Venus , masse = 4871e21 , texture ='https://media.gettyimages.com/photos/planet-venus-picture-id85758378' , make_trail = Trail , pos_init = p_Venus , periode_theo = 224.70)
Terre = sphere(name = 'Terre' , pos = p_Terre , vit = v_Terre , radius = 12756e3*K*K_Terre , masse = 5974e21 ,  texture = "http://i.imgur.com/rhFu01b.jpg" , make_trail = Trail , pos_init = p_Terre , periode_theo = 365.26)
Mars = sphere(name = 'Mars' , pos = p_Mars , vit = v_Mars , radius = 6794e3*K*K_Mars , masse = 641e21 , texture = 'https://i.imgur.com/S1KPJaR.jpg' , make_trail = Trail , pos_init = p_Mars , periode_theo = 686.98)
Jupiter = sphere(name = 'Jupiter' , pos = p_Jupiter , vit = v_Jupiter , radius = 142800e3*K*K_Jupiter , masse = 1899000e21 , texture = 'https://i.imgur.com/SHUNJ9mb.jpg' , make_trail = Trail , pos_init = p_Jupiter , periode_theo = 4332.7)
Saturne = sphere(name = 'Saturne' , pos = p_Saturne , vit = v_Saturne , radius = 120000e3*K*K_Saturne , masse = 568000e21 , texture = 'https://i.imgur.com/jLS3Lce.jpg' , make_trail = Trail , pos_init = p_Saturne , periode_theo = 10759.5)
Uranus = sphere(name = 'Uranus' , pos = p_Uranus , vit = v_Uranus , radius = 51120e3*K*K_Uranus , masse = 86760e21 ,  texture = 'https://i.imgur.com/4I8jk93.jpg' , make_trail = Trail , pos_init = p_Uranus , periode_theo = 30685)
Neptune = sphere(name = 'Neptune' , pos = p_Neptune , vit = v_Neptune , radius = 49528e3*K*K_Neptune , masse = 103000e21 , texture = 'https://media.gettyimages.com/photos/neptune-picture-idST000287' , make_trail = Trail , pos_init = p_Neptune , periode_theo = 60190)

Comete_Halley = ellipsoid(name = 'Halley' , pos = p_Comete_Halley, vit = v_Comete_Halley, length=40e6*K*K_Comete, height=10e6*K*K_Comete, width=10e6*K*K_Comete,axis = axe_comete_Halley, masse =1.014e12,make_trail = Trail, color=color.cyan, pos_init = p_Comete_Halley , periode_theo = 27792)
Comete_Tempel = ellipsoid(name = 'Tempel' , pos = p_Comete_Tempel, vit = v_Comete_Tempel, length=40e6*K*K_Comete, height=10e6*K*K_Comete, width=10e6*K*K_Comete,axis = axe_comete_Tempel, masse =7.2e13,make_trail = Trail, color=color.orange, pos_init = p_Comete_Halley , periode_theo = 2029.4)
Comete_Tchouri = ellipsoid(name = 'Tchouri' , pos = p_Comete_Tchouri, vit = v_Comete_Tchouri, length=40e6*K*K_Comete, height=10e6*K*K_Comete, width=10e6*K*K_Comete,axis = axe_comete_Tchouri, masse =1e13,make_trail = Trail, color=color.green, pos_init = p_Comete_Tchouri , periode_theo = 2352.3)



SystemeSolaire = [Soleil,Mercure,Venus,Terre,Mars,Jupiter,Saturne,Uranus,Neptune,Comete_Halley,Comete_Tempel,Comete_Tchouri]
Planetes = SystemeSolaire[1:]

Liste_Comete = [Comete_Halley,Comete_Tempel,Comete_Tchouri]


###############################################################################
# Légendes (pour afficher les périodes des planètes)
###############################################################################

L_Mercure = label(pos = Mercure.pos)
L_Venus = label(pos = Venus.pos)
L_Terre = label(pos = Terre.pos)
L_Mars = label(pos = Mars.pos)
L_Jupiter = label(pos = Jupiter.pos)
L_Saturne = label(pos = Saturne.pos)
L_Uranus = label(pos = Uranus.pos)
L_Neptune = label(pos = Neptune.pos)


Legendes = [L_Mercure,L_Venus,L_Terre,L_Mars,L_Jupiter,L_Saturne,L_Uranus,L_Neptune]


###############################################################################
# Fonctions mécaniques Verlet
###############################################################################


def acc2(p1,M,p2):        # Acceleration exercée par 2 sur 1
    global G
    p1p2 = p2 - p1
    r12 = mag(p1p2)
    return (G*M / (r12**3) ) * p1p2


def acceleration(planete1):     # Calcul de l'accélération de la planete à l'instant t
    global SystemeSolaire
    A = vec(0,0,0)
    for planete2 in SystemeSolaire:
        if planete1 != planete2:
            A = A + acc2(planete1.pos , planete2.masse , planete2.pos)
    return A


def nv_acceleration(planete1):     # Calcul de l'accélération de la planete à l'instant t+dt
    global SystemeSolaire
    A = vec(0,0,0)
    for planete2 in SystemeSolaire:
        if planete1 != planete2:
            A = A + acc2(planete1.nv_pos , planete2.masse , planete2.nv_pos)
    return A


def pos_suivante(SystemeSolaire,dt):           # Calcul de la position suivante de la planete
    for planete in SystemeSolaire:
        planete.nv_pos = planete.pos + planete.vit*dt + acceleration(planete)*(dt**2)/2


def rotation_planetes(dt):          # pas les bonnes vitesses mais elles sont proportionnelles par rapport à la réalité
    Soleil.rotate (angle = (2*pi)/(22*dt), axis =vec(0,0,1))
    Mercure.rotate (angle = (2*pi)/(59*dt), axis =vec(0,0,1))
    Venus.rotate (angle = (2*pi)/(243*dt), axis =vec(0,0,-1))   # -1 car rotation ds le sens inverse
    Terre.rotate (angle = (2*pi)/dt , axis = vec(0,0,1))
    Mars.rotate (angle = (2*pi)/(1.025*dt), axis =vec(0,0,1))
    Jupiter.rotate (angle = (2*pi)/(0.41*dt), axis =vec(0,0,1))
    Saturne.rotate (angle = (2*pi)/(0.426*dt), axis =vec(0,0,1))
    Uranus.rotate (angle = (2*pi)/(0.72*dt), axis =vec(0,1,0))  # axe différent, Uranus a un axe de rotation incliné de 90°
    Neptune.rotate (angle = (2*pi)/(0.76*dt), axis =vec(0,0,1))
    for planete in Liste_Comete :
        planete.height = 10e6*K*K_Comete
        planete.width = 10e6*K*K_Comete
        planete.axis = 40e6*K*K_Comete * planete.pos / mag(planete.pos)
    



def mouvement(SystemeSolaire,Planetes,Legendes,dt):     # fonction de mouvement des planètes
    pos_suivante(SystemeSolaire,dt)
    
    for planete in SystemeSolaire:
        
        a_i1 = acceleration(planete)
        a_i2 = nv_acceleration(planete)
        nv_vit = planete.vit + (a_i1 + a_i2)*dt/2
    
        planete.pos = planete.nv_pos + vec(0,0,0)   #permet d'éviter la copie liée à l'origine
        planete.vit = nv_vit
    
    rotation_planetes(dt)   # Rotation des planetes


###############################################################################
# Fontions de mesure
###############################################################################


def mesures_init(Planetes):             # Initialisation des différentes mesures sur les planetes (hors Soleil)
    for planete in Planetes:
        planete.periode = 0
        planete.periode_t0 = 0
        planete.ecart = UA
        planete.ecart_t0 = UA
        planete.perihelie = planete.pos_init + vec(0,0,0)   #permet d'éviter la copie liée
        planete.aphelie = planete.pos_init + vec(0,0,0)     #permet d'éviter la copie liée



def mesures(Planetes,t,t0,n):              # Calcul des mesures sur les planètes (Soleil exclu)
    
    for planete in Planetes:
        

        if mag(planete.pos - Soleil.pos) < mag(planete.perihelie - Soleil.pos):     # perihelie (prob)
            planete.perihelie = planete.pos + vec(0,0,0)    #permet d'éviter la copie liée
        
        if mag(planete.pos - Soleil.pos) > mag(planete.aphelie - Soleil.pos):       # aphelie (prob)
            planete.aphelie = planete.pos + vec(0,0,0)      #permet d'éviter la copie liée
        
        
        
        if -1/n < t - t0 < 1/n:               # position de la planete à t = t0
            planete.pos_t0 = planete.pos + vec(0,0,0)       #permet d'éviter la copie liée
            trail_on()
        
        
        if 0.8*planete.periode_theo  <  t  <  1.2*planete.periode_theo:      # Calcul de periodes et ecarts à partir de t = 0
            if mag(planete.pos - planete.pos_init) < planete.ecart:
                planete.periode = t
                planete.ecart = mag(planete.pos-planete.pos_init)
        
        
        if 0.8*planete.periode_theo  <  t-t0  <  1.2*planete.periode_theo:   # Calcul de periodes et  ecarts à partir de t = t0
            if mag(planete.pos-planete.pos_t0) < planete.ecart_t0:
                planete.periode_t0 = t - t0
                planete.ecart_t0 = mag(planete.pos - planete.pos_t0)
    
    
    Legende_scene = "\nTemps en années : " + str(t/365.26)  + "\nTemps en jours : " + str(t) + "\n"   # Affichage du temps (années et jours)
    Legende_scene += "\nDate t0 (en jours) : " + str(t0) +"\nPas pour chaque itération (en jours) : " + str(1/n) + "\n"
    
    for planete in Planetes:
        Legende_scene += "\nDistance périhélie de " + planete.name + " : " + str("%.2e" % mag(planete.perihelie))
        Legende_scene += "\nDistance aphélie de " + planete.name + " : " + str("%.2e" % mag(planete.aphelie))
        Legende_scene += "\nPériode de " + planete.name + " : " + str(planete.periode)
        Legende_scene += "\nPériode de " + planete.name + " (calculée à partie de t0) : " + str(planete.periode_t0)
        Legende_scene += "\nEcart de distance sur la première période de " + planete.name + " : " + str("%.2e" % planete.ecart)

        Legende_scene += "\n"

    scene.caption = Legende_scene

    i_planete=0                 # Affichage des periodes dans l'espace en 3D
    for legende in Legendes:
        legende.text = str(Planetes[i_planete].periode)
        i_planete += 1





###############################################################################
# Fonctions annexes
###############################################################################

def trail_on():             # Fonction d'activation des trajectoire (inutilisée)
    for planete in SystemeSolaire:
        attach_trail(planete, color = planete.color).start


###############################################################################
# Programme
###############################################################################


t=0
i = 0
mesures_init(Planetes)          # Création des variables de mesure




while True:
    rate(nb_boucles)          # Nb de boucles par seconde
    
    
    mesures(Planetes,t,t0,n)
    mouvement(SystemeSolaire,Planetes,Legendes,dt)
    i += 1                      # itération (n itération = 1 jour)
    t = i/n                     # temps en journées (1/n jour supplémentaire par boucle)






