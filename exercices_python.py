# Exercice 1: écrire 3 variable (a,b,c) avec comme valeurs respective 1,"France", 36.2 et les affichés dans la console

#a = 1
#b = "France"
#c = 36,2

#print (a, b, c)

# Exercice 2: écrire une variable ch avec comme valeur "salut" changé sa valeur avec "ça va ?" puis affiché la variable dans la console.

#ch = "salut"
#ch ="ça va ?"

#print (ch)

# Exercice 3: déclarer deux variables x et y, avec 3 et 8,5, convertissez les en chaine de charactère puis affiché les avec leurs type dans la console.

#x = 3
#y = 8,5

#x = str(x)
#y = str(y)

#print(x, type(x))
#print(y, type(y))

# Exercice 4: Ecrire un programme qui demande le poids en Kg, le stocker dans une variable puis l'afficher.

#poid = ""

#poid = input ("Quel est votre poids ? ( en Kg) ")

#print (" Votre poids est de " + poid + " Kg !" )

# Exercice 5: Ecricre une variable Var contenant "Bonjour" si c'est une chaine de caractère affiché "chaine de caractère" sinon si c'est un entier affiché "entier".

#var = "Bonjour"

#if type(var) == str :
    #print("Chaine de caractère")
#elif type(var) == int:
    #print("Entier")
#else:
    #print("Inconnu")

# Exercice 6: Déclarer un chiffre positif ou négatif, si il est positif afficher Positif sinon affiché Négatif.

#chiffre = 0

#chiffre = int(input("Donnez un chiffre positif ou négatif ?"))

#if chiffre >= 0:
    #print("Positif")
#else :
    #print("négatif")

# Exercice 7: Créer une variable pour demander l'age, vérifier si l'utilisateur est mineur ou majeur , puis afficher le résultat dans la console.

#age = int(input("Quel age avez-vous ?   "))

#if age >= 18 : 
    #print("Vous êtes majeur !")
#else:
    #print("Vous êtes mineur..")

# Exercice 8: Ecrire deux programmes pour afficher des nombre de 1 à 20, l'un avec une boucle while l'autre avec une boucle for

# version while
#compteur = 1

#while compteur <= 20:

    #print (compteur)
    #compteur += 1

# version for

#for i in range(1,21):
    #print(i)

# Exercice 9: comme l'exercice 8 mais en affichant les nombres impaires

# version while
#compteur = 1

#while compteur <= 21:

    #if compteur % 2 == 1:
        #print (compteur)
    #compteur += 1

# version for

#for i in range(1,21):
    #if i % 2 == 1:
        #print(i)

# Exercice 10: création d'une liste par compreension

#liste = [i for i in range (1,11)]
#print (liste)

# Exercice 11: création d'une liste par nombre paire

#liste = [i for i in range (1,21) if i % 2 == 0]
#print(liste)

# Exercice 12: Trier la liste l contenant [8,6,3,4,1,12,2,9.2], puis afficher la liste.

#l = [8,6,3,4,1,12,2,9.2]
#liste = sorted(l)
#print(liste)

# Exercice 13: écrire le nombre d'occurrence du nombre 1 de la liste l

#l = [3,2,2,1,9,1,2,3,7]

#print(l.count(1))

# Exercice 14: Ajout d'élément à une liste

#l = []

#l += [10,25,30,45,90,"ab","cd","ef"]

#print(l)

# Exercice 15: Compréhension de liste

#L = [1,2,3,4,5,6,7,8,9,10]

#L1 = []

#for i in range(len(L)):
    #if i%3 == 0:
        #L1.append(L[i])
#print(L1)

# Exercice 16: Trer une chaine de caractère

#c = "france"

#print(sorted(c))

# Exercice 17: Elements en commun entre deux listes

#L1 = [9,8,7,14,3,2,"a","p","bonjour","b"]
#L2 = ["b", 1, 9.2, 6, 3, 9, "p"]
#L3 = set(L1).intersection(set(L2))
#L3 = list(L3)

#print(L3)

# Exercice 18: Trier une liste de tuple

#L = [("Pomme", 15), ("Banane", 8), ("Fraise", 12), ("Kiwi", 9), ("Peche", 2)]

#L.sort(key = lambda x : x[1])

#print (L)

# Exercice 19: Inverser une chaine

#ch = "Bonjour tout le monde"

#ch_inverse = ch[::-1]

#print (ch_inverse)

# Exercice 20: Les valeurs d'un dictionnaire

#d = {"Pomme":3, "Banane":7, "Kiwi":1}

#print(d["Pomme"])
#print(d["Banane"])

# Exercice 21: Somme des valeurs d'un dictionnaire

#d = {"Pomme":3, "Banane":7, "Fraise":12, "Kiwi":1, "Peche":2}

#sum(d.values())

# Exercice 22: Utilisation de la méthode format()

#nombre = float("{:.2f}".format(187.632587))

#print(nombre)

# Exercice 23: Autre utilisation de la méthode format()

#monNom = "Charles"
#age = 33
#nomLangage = "Python"

#phrase = f"Je m'appelle {monNom} et j'ai {age} ans. J'apprends le langage {nomLangage}".format(monNom,age,nomLangage)

#print(phrase)

#Exercice 24: afficher une table de multiplication

#choixDuChiffre = int(input("Quel table voulez-vous voir ?  "))

#for i in range (0,11):
    #print(f"{choixDuChiffre} x" ,i,"=", choixDuChiffre*i)

# Exercice 25: Ecrire un programme affichant le dossier dans lequel il se trouve

#import os
#print(os.getcwd())

# Exercice 26: Suprimer un élément d'une liste

#liste = [1,2,3,4,5]

#liste.pop(0)

#print(liste)

# Exercice 27: Récupérer l'extension d'un fichier

#import os
#chemin_fichier = r'C:\Users\Charles\Documents\exercices_python\exercices_python.py'
## récupérer le nom du fichier i.e exercices_python.py
#nom_fichier = os.path.basename(chemin_fichier)
## convertir le nom du fichier en liste, puis on récupère
## le dernier élément de cette liste qui représente
## l'estension 
#extension_fichier = nom_fichier.split(".")[-1]
#print("Extension fichier : ", extension_fichier)

# Exercice 28: calculer le temps d'execution d'un script

#import time

## Stocker le temps de début
## du programe
#debut = time.time()

##### LE CODE #####
#for i in range(0,11):
    #print("8 x", i ,"=", 8*i)
######################

## Stocker le temps de fin de programme

#fin = time.time()

## Calculer le temps d'exécution

#print("Temps d'exécution du code : ", fin-debut)

# Exercice 29: Ecrire un programme qui permet de mélanger aléatoirement les éléments d'une liste

#import random

#L = [3,6,8,7,2,"s","ch","d"]
#print(L)

#random.shuffle(L)
#print(L)

# Exercice 30: Générer aléatoirement un nombre entre 20 et 30

#import random

#nombre_aleatoire = random.randint(20,30)

#print(nombre_aleatoire)

# Exercice 31: Affichege de motifs

#for i in range(8):
    #for y in range(5,21):
        #print(y, end = " ")
    #print()

# Exercice 32: 

#L = [3,6,9,12,15,18,21,24]

#L1 = [l/3 for l in L]
#print (L1)

# Exercice 33:

#L = [-6.5,-3,-1,2,8,-3.6]

#L1 = [l for l in L if l>0]
#print (L1)

# Exercice 34: fonction mathématique

#def f(a,b,x):

    #return a*(x**3)+2*a*(x**2)+b

#print(f(3,0,1))
#print(f(0,2,2))

# Exercice 35: présence d'un élément dans une liste

#def VerifPresence(a,L):
    #if a in L:
        #return True
    #else:
        #return False
    
#print (VerifPresence(2,[1,2,3,4,5,6]))
#print (VerifPresence(-1,[3,6,9,7,"abcr"]))

# Exercice 36: Calcule de la somme des chiffre

#nombre = int(input("entrer un nombre : "))

#nombre = str(nombre)
#somme = 0

#for chiffre in nombre:
    #somme += int(chiffre)

#print(f"La somme des chiffre de {nombre} est : {somme}")

# Exercice 37: Somme d'une liste

#def calculSomme(L):
    #somme = 0
    #for nombre in L:
        #somme += nombre
    #return somme

#print (calculSomme([3,2,6,9,-1.5]))
#print (calculSomme([-3,-6,0,1,2,7]))

# Exercie 38: Suppression des doublons

#def supprimerDoublons(L):
    #for element in L:
        #elementDoublon = L.count(element)
        #if elementDoublon >= 2:
            #for i in range(elementDoublon-1):
                #L.remove(element)

    #L.sort()
    #return L

#print(supprimerDoublons([0,3,5,7,3,5,1,-1]))
#print(supprimerDoublons([0,5,9,10,3.2,1,-3]))

# Exercice 39: Ajout d'éléments dans un dictionnaire

#def ajoutElementDict(cle,valeur,d):
    #d[cle] = valeur
    #return d

#print(ajoutElementDict("baptiste",29,{"julien":14,"laurent":31}))
#print(ajoutElementDict("poids", 65.3,{}))

# Exercice 40: Recréaton de la fonction max

#def maximum(L):
    #max_L=L[0]
    #for element in L:
        #if element > max_L:
            #max_L = element
    #return max_L

#print(maximum([-9,2,4,1,8]))
#print(maximum([-3,1,7,2,3]))

# Exercice 41: Somme d'une sous liste

#def sommeSousListe(L,i,j):
    ## Sélectionner la sous liste
    #lij = L[i:j+1]
    ## Initialiser la variable où on va stocker la somme
    #somme = 0

    #for element in lij:
        #somme += element
    #return somme

#print(sommeSousListe([4,10,12,16,18],2,4))
#print(sommeSousListe([2,4,6,8,10,12],0,2))

# Exercice 42: Création de motifs

#x = 0
#while x <= 6:
    #print ("*"*x)
    #x += 1

## ou 

#for nombreEtoile in range(1,11):
    #if nombreEtoile%2 == 0 or nombreEtoile == 1:
        #print("*"*nombreEtoile)

# Exercice 43: Recréation de la fonction Min

#def minimum(L):
    #min_L=L[0]
    #for element in L:
        #if element < min_L:
            #min_L = element
    #return min_L

#print(minimum([-9,2,4,1,8]))
#print(minimum([1,7,6,2,3,-3,-12]))

# Exercice 44: Recréation de la fonction Len

#def longueur(L):
    #taille_L = 0
    #for element in L:
        #taille_L +=1
    #return taille_L

#print(longueur([3,6,7,"abde",[1,3,57],True]))
#print(longueur([]))

# Exercice 45: Calcul de la moyenne d'une liste

#def moyenneList(L):
    #somme_L = 0
    #for element in L:
        #somme_L += element
    #moyenne_L = somme_L / len(L)
    #return moyenne_L

#print(moyenneList([1,2,3,4,5,6,7]))
#print(moyenneList([3,0,-1,5,6,9,17]))

# Exercice 46: Les diviseurs d'un nombre entiers

#def diviseur(n):
    ## la liste qui va contenir tous les diviseur
    #n_diviseur = []
    ## parcourir tous les éléments de 1 à n
    #for div in range(1,n+1):
        ## si le reste de la division de n par div est 0
        #if n%div == 0:
            ## alors div est un diviseur de n
            ## et on le rajoute dans la liste des diviseurs
            #n_diviseur.append(div)
    #return n_diviseur

#print(diviseur(3))
#print(diviseur(9))

# Exercice 47: Vérification de majuscule

#def verifMaj(phrase):
    #for lettre in phrase:
        #if lettre.isupper():
            #return True
    #return False

#print(verifMaj("Les légumes sont bon pour la santé"))
#print(verifMaj("j'apprends le langage java"))

# Exercice 48: Concaténation de liste

#def concateListe(L1,L2,L3):
    #L_concate = L1+L2+L3
    #return L_concate

#print(concateListe([0,9,8],[2,6,9],[True,False,"abc"]))

# Exercice 49: Calcule du nombre de valeur d'un dictionnaire

#def nbrValeurDict(d):
    ## extraire la liste des clés
    ## dans le dictionnaire
    #d_cle = list(d.keys())
    ## initialisation de la variable
    ## qui va contenir le nombre de valeur
    ## du dictionnaire d
    #nombre_valeur = 0
    ## parcourir toutes les clés
    #for cle in d_cle:
        ## pour chaque clé, déterminer le nombre
        ## de valeur contenus dans la liste associée
        ## à cette clé
        #longueur_val = len(d[cle])
        ##ajouter ce nombre de valeur à la variable nombre_valeur
        #nombre_valeur += longueur_val
    #return nombre_valeur

#print(nbrValeurDict({"a":[1,2,3],"b":[3,"p"],"c":[8]}))

# Exercice 50: Concaténation de dictionnaire

#def concatDict(d1,d2):
    #d1.update(d2)
    #return d1

#print(concatDict({"a":3,"b":6},{"c":2,"d":-1}))

# Exercice 51: Calcul de la factorielle d'un nombre

#def calculeFactorielle(n):
    ## factoriel de n = n x (n-1) x (n-2) x ..... x 2 x 1

    ## la factorielle du nombre 0 = 1
    #if n == 0:
        #return 1
    ## la variable qui va contenir
    ## notre résultat final
    #resultat_factoriel = n
    ## on parcours tous les éléments de n-1 à 1
    #for k in range(n-1,0,-1):
        #resultat_factoriel = resultat_factoriel * k
    #return resultat_factoriel

#print(calculeFactorielle(0))
#print(calculeFactorielle(9))
#print(calculeFactorielle(3))

# Exercice 52: Diviseurs & multiple

#def diviseurMult(n,a,nbrSeuil):
    #resultat = []
    ## Parcourir les nombres de 0 et nbrSeuil
    #for nbr in range(nbrSeuil+1):
        ## le reste de la division de nbr par n doit être égale à 0
        ## et le reste de la division de nbr par a doit être différente de 0
        #if nbr%n == 0 and nbr%a != 0:
            ## si les conditions sont satisfaites, alors
            #resultat.append(nbr)
    #return resultat

#print(diviseurMult(5,2,100))
#print(diviseurMult(11,3,85))

# Exercice 53: Présence d'une voyelle dans une chaine

#def presenceVoyelle(phrase):
    ## la liste des voyelles
    #voyelles = ["a","e","i","o","u","y"]
    ## parcourir toutes les voyelles dans la phrase passé
    #for voyelle in voyelles:
        ## si la voyelle existe dans la phrase passée en paramètres
        #if voyelle in phrase:
            #return True
    #return False

#print(presenceVoyelle("Je vais prendre ma douche"))
#print(presenceVoyelle("rbhpm"))

# Exercice 54: Suppression des espaces dans une phrase

#def supprEspace(phrase):
    #L_phrase = phrase.split(" ")
    #phraseSansEspace = "".join(L_phrase)
    #return phraseSansEspace

#print(supprEspace("La france est belle"))
#print(supprEspace("Je vais prendre mon vélo"))

# Exercice 55: Position d'un élément dans une liste

#def positionEltListe(L,x):
    #x_indices = []
    #for i in range(len(L)):
        ## si un élément de L est égale à i
        #if L[i] == x:
            ## ajouter son index à la liste des indices
            #x_indices.append(i)
    ## si la liste est vide, x n'existe pas dans L
    #if len(x_indices) == 0:
        #print("L'élément ",x," n'éxiste pas dans la liste ",L)
    #return x_indices

#print(positionEltListe([1,2,3,6,8,7,3],3))
#print(positionEltListe([6,8,9,1,3,7],-1))

# Exercice 56: Filtrer les mots suivant leur longueur

#def filtrerMots(phrase,longueurMini):
    ## convertir la phrase en utilisant comme séparateur un "espace"
    #phrase_liste = phrase.split(" ")
    ## variable qui va contenir la phrase filtré
    #phrase_filtre =[]

    #for mot in phrase_liste:
        #if len(mot) >= longueurMini:
            ## alors on ajoute ce mot à notre nouvelle liste
            #phrase_filtre.append(mot)
    ## convertir la liste en chaine de caractère en gardant un espace entre les mots
    #phrase_filtre = " ".join(phrase_filtre)
    #return phrase_filtre

#print(filtrerMots("Salut toi !", 4))
#print(filtrerMots("Quel est ton origine ?", 5))

# Exercice 57: Inverser l'ordre des mots

#def inverserPhrase(phrase):

    #phrase_liste = phrase.split(" ")
    #phrase_liste.reverse()
    #phrase = " ".join(phrase_liste)
    #return phrase

#print(inverserPhrase("Bonjour tout le monde ! ça va ?"))
#print(inverserPhrase("Pomme de pin, pomme de terre"))

# Exercice 58: Nombre d'occurence dans une liste

#def nombreOccurrence(L):

    #resultat_tuples = []

    #for element in L:
        #nombre_occurrence = L.count(element)
        #tuple_element = (element,nombre_occurrence)

        #if tuple_element not in resultat_tuples:
            #resultat_tuples.append(tuple_element)
    #return resultat_tuples

#print(nombreOccurrence([-4,8,-3,2,1,2,7,9,-3,8,1]))
#print(nombreOccurrence(["a",3,4,"b","a",3]))

# Exercice 59: Union de liste sans duplication

#def unionListe(L1,L2,L3):

    #ens1 = set(L1)
    #ens2 = set(L2)
    #ens3 = set(L3)

    #unionEnsemble = ens1 | ens2 | ens3 

    #l_union = list(unionEnsemble)
    #l_union.sort()

    #return l_union

#print(unionListe([3,6,9,3],[1,0,3],[12,6,0]))

# Exercice 60: Calcule du PGDC ( Plus Grand Diviseur Commun)

#def calculePGDC(a,b):
    ## Vérifier si les 2 paramètres a et b sont positifs
    ## Si ce n'est pas le cas, retourner une erreur
    #assert(a>0 and b>0)
    ## tant que b est différent de 0
    #while b != 0:
        ## double affectation
        ## "a" on lui affecte "b"
        ## "b" on lui affecte le "reste de a divisé par b"
        #a,b = b, a%b
    ## on retourne "a" à la fin
    #return a


#print(calculePGDC(3,5))
#print(calculePGDC(5,15))

# Exercice 61: lecture d'un fichier

#def lireFichier(cheminFichier):
    ## ouverture du fichier en mode lecture
    #fichier = open(cheminFichier,"r")
    ## Lecture du contenu du fichier
    #contenu = fichier.read()
    ## fermeture du fichier
    #fichier.close()
    ## retourner le contenu du fichier
    #return contenu

#lireFichier(r"C:\Users\Charles\Documents\exercices_python\test.txt")

# Exercice 62: Nombre d'occurence d'un mot dans un fichier

#def nbrOccFichier(cheminFichier,mot):
    ## ouverture d'un fichier en mode lecture
    #fichier = open(cheminFichier, "r")
    ## lecture de tout le contenu
    #contenu = fichier.read()
    ## convertir le contenu du fichier en liste de mots
    #liste_mots = contenu.split(" ")
    ## initialiser la variable qui stock l'occurence du mot
    #occ_mot = 0
    ## parcourir tous les mots dans la liste
    #for element in liste_mots:
        ## si l'élément de la liste est égale au mot recherché
        #if element == mot:
            ## incrémenté occ_mot de 1
            #occ_mot += 1
    #return occ_mot

#print (nbrOccFichier(r"C:\Users\Charles\Documents\exercices_python\test.txt","je"))

# Exercice 63: Supprimer un caractère d'un fichier

#def suppCarac(cheminFichier, caractere):
    ## L'utilisation de la syntaxe with open permet de fermer automatiquement le fichier
    #with open(cheminFichier, "r") as fichier:
      #contenu = fichier.read()
    ## remplacer le caractère par un vide
    #nouveau_contenu = contenu.replace(caractere, "")

    ## ouverture du fichier en écriture
    #with open(cheminFichier, "w") as fichier:
      ## écrire le nouveau contenu
      #fichier.write(nouveau_contenu)
    
    #return


#print(suppCarac(r"C:\Users\Charles\Documents\exercices_python\test.txt", ","))

# Exercice 64: présence d'un nombre dans un fichier

#def presenceNombre(cheminFichier):
    #fichier = open(cheminFichier, "r")
    #contenu = fichier.read()

    #for c in contenu:
        ## vérifier le caractère
        #if c.isdigit():
            #return True
    #return False    


#print(presenceNombre(r"C:\Users\Charles\Documents\exercices_python\test.txt"))

# Exercice 65: Nombre de fichier dans un dossier

#import os

#def nombreFichier(cheminDossier):
    ## initiaisation du compteur
    #nombre_fichier = 0
    ## lister tout le contenu du dossier
    #listing_contenu = os.listdir(cheminDossier)
    ## Parcourir le contenu du dossier
    #for contenu in listing_contenu:
        ## si le contenu est un fichier
        #if os.path.isfile(os.path.join(cheminDossier, contenu)):
            ## Incrémenter la variable nombre_fichier
            #nombre_fichier += 1
    #return nombre_fichier

#print(nombreFichier(r"C:\Users\Charles\Documents\exercices_python"))

# Exercice 66: Ecrire dans un fichier

#def ecrireFicher(cheminFichier, texte):
    ## ouverture d'un fichier en écriture
    #f = open(cheminFichier,"w")
    ##écriture du texte placé en paramètre dans le fichier
    #f.write(texte)
    ## fermeture
    #f.close()

#monChemin = r"C:\Users\Charles\Documents\exercices_python\test.txt"
#monTexte = "J'apprend Python !"

#ecrireFicher(monChemin, monTexte)

# Exercice 67: La clé avec le nombre de valeur unique maximale

#def cleMaxValeurDict(d):
    #cle_val = []
    ## listing des clées du dictionnaire
    #d_cles = list(d.keys())
    ## Parcourir toutes les clé du dictionnaire
    #for cle in d_cles:
        ## Le nombre de valeur associé à la clé sans compter les doublons
        #nombre_valeurs_unique = len(set(d[cle]))
        ##ajouter le tuple (cle, nombre valeur unique)
        #cle_val.append((cle, nombre_valeurs_unique))

    ## tier suivant le 2eme élément au tuple
    #cle_val.sort(key = lambda x : x[1])
    ##Extraire la clé ayant le nombre maximal
    #cle_max_val = cle_val[-1][0]
    #return cle_max_val

#print(cleMaxValeurDict({"a":[9,10,9,7,3,1],"b":[5,3,2,2,2],"c":[1,1,1,1,1,1,8,2]}))

# Exercice 68: Demander une liste à l'utilisateur

#liste_utilisateur = []

## Demander le nombre d'éléments que la liste doit contenir
#nombre_element = int(input("Entrez le nombre d'élément de la liste :"))
## Demander autant de nombre nécessaire pour remplir la liste
#for i in range (nombre_element):
    #element = int(input("Entrez un élément de la liste : "))
    ## ajouter cet élément à la liste
    #liste_utilisateur.append(element)

#print (liste_utilisateur)

# Exercice 69: Nombre de jour et heures

from datetime import datetime

def nbrJourHeure(dateDebut, dateFin):
    ## le format de la date
    format_date = "%Y/%m/%d"
    ## convertir la date de début de string à un format date
    date_debut_formate = datetime.strptime(dateDebut,format_date)
    ## convertir la date de fin de string à un format date
    date_fin_formate = datetime.strptime(dateFin,format_date)
    ## Nombre de jour entre date début et date fin
    nombreJour = (date_fin_formate - date_debut_formate).days
    ## calcul du nombre d'heures
    nombreHeure = nombreJour * 24

    return nombreJour, nombreHeure

print(nbrJourHeure("2022/05/15","2022/06/20"))
print(nbrJourHeure("2022/04/1", "2022/04/27"))