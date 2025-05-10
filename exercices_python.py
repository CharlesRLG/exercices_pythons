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

#from datetime import datetime

#def nbrJourHeure(dateDebut, dateFin):
    ## le format de la date
    #format_date = "%Y/%m/%d"
    ## convertir la date de début de string à un format date
    #date_debut_formate = datetime.strptime(dateDebut,format_date)
    ## convertir la date de fin de string à un format date
    #date_fin_formate = datetime.strptime(dateFin,format_date)
    ## Nombre de jour entre date début et date fin
    #nombreJour = (date_fin_formate - date_debut_formate).days
    ## calcul du nombre d'heures
    #nombreHeure = nombreJour * 24

    #return nombreJour, nombreHeure

#print(nbrJourHeure("2022/05/15","2022/06/20"))
#print(nbrJourHeure("2022/04/1", "2022/04/27"))

# Exercice 70: Générer aléatoirement un mot de passe

#import string
#import random

## création d'une liste de caractère à partir de laquelle nous allons générer notre mot de passe aléatoirement
#liste_caractere = list(string.ascii_letters + string.digits + "!@#$%^&*()")

#def genererMDP(caractere,tailleMDP):
    ## mélanger aléatoirement les caractères
    #random.shuffle(caractere)
    ## création de la liste qui va contenir notre mot de passe
    #mot_de_passe = []
    ## choisir aléatoirement les caractère du mot de passe jusqu'à atteindre la taille passé en paramètres
    #for i in range(tailleMDP):
        #carac_alea = random.choice(caractere)
        ## ajouter le caractère choisi aleatoirement dans la liste mot de passe
        #mot_de_passe.append(carac_alea)
    
    ## mélanger encore une fois ntre liste qui va contenir notre mot de passe
    #random.shuffle(mot_de_passe)
    ## convertir la ligne en chaine de caractère sans espace entre les caractères
    #mot_de_passe = "".join(mot_de_passe)

    #return mot_de_passe

#print(genererMDP(liste_caractere,10))

# Exercice 71: Fonction Trigonométrique
#import math

#def foncTrigo(x):
    ## définition de la fonction à calculer
    #f = math.cos(x)*math.sin(x) + math.sin(x) + 8
    #return f

#print(foncTrigo(math.pi/4))

#print(foncTrigo(math.pi))

# Exercice 72:

#liste_entiers = []

## parcourir tous les nombres entre 100 et 999
#for nombre in range(100,1000):
    ## convertir le nombre en chaine de caractère
    #str_nombre = str(nombre)
    ## sommer les chiffres du nombre
    #somme_chiffre = int(str_nombre[0]) + int(str_nombre[1]) + int(str_nombre[2])
    ## faire le produit des chiffre du nombre
    #produit_chiffre = int(str_nombre[0]) * int(str_nombre[1]) * int(str_nombre[2])
    ## si le reste de la division de produit_chiffre par somme_chiffre est égale à 0
    #if produit_chiffre % somme_chiffre == 0:
        ## alors ajouter le nombre dans la liste des entiers
        #liste_entiers.append(nombre)

#print(liste_entiers)

#Exercice 73: 

#def calculSomme(L):
    ## si la fonction est vide
    #if len(L) == 0: ## ou if not L
        ## retourner 0
        #return 0
    ## sinon calculer la somme en utilisant la récursivité
    #return L[0] + calculSomme(L[1:])

#print(calculSomme([3,2,6,9,-1,5]))
#print(calculSomme([-3,-6,0,1,2,7]))

#Exercice 74: 

#def suiteFibonacci(N):
    ## si le nombre N passé en paramètre est inférieur ou égal à 2
    #if N<=2:
        ## le résultat de la suite est égale à 1
        #return 1
    ## sinon faire appel à la même fonction en faisant appel à la récursivité
    #return suiteFibonacci(N-1) + suiteFibonacci(N-2)

#print(suiteFibonacci(25))

# Exercice 75: Fonction récursive mutuelle

#def nombrePair(N):
    ## si le nombre passé en paramètre est égal à 1
    #if N == 1:
        ## alors il n'est pas pair
        #return False
    ## sinon faire appel à la fonction impaire
    #return nombreImpair(N-1)

#def nombreImpair(N):
    ## si le nombre passé est égal à 1
    #if N == 1:
        ## alors N est impair
        #return True
    ## sinon faire appel à la fonction nombrePair en N-1
    #return nombrePair(N-1)

#print(nombrePair(5))
#print(nombrePair(6))

# Exercice 76: Recréation de la méthode join()

#def join(L,caractere):
    #chaine_carac =  ""
    #for i in range(len(L)):
        #chaine_carac += L[i]
        #if i != len(L)-1:
            #chaine_carac += caractere
    #return chaine_carac

#print(join(["bonjour","Aurélie"],"ici"))
#print(join(["2","3","4","1","33","44"],"9"))

# Exercice 77:recréation de la méthode replace()

#def remplacer(phrase,ancienMot,nouveauMot):
    #if ancienMot in phrase:
        #debut_ancienMot_index = phrase.index(ancienMot)
        #fin_ancienMot_index = debut_ancienMot_index + len(ancienMot)
        #phrase_list = list(phrase)
        #phrase_list[debut_ancienMot_index:fin_ancienMot_index] = nouveauMot
        #phrase = "".join(phrase_list)
    #return phrase

#print(remplacer("Bonjour Aurelie", "Aurelie","Justine"))
#print(remplacer("J'ai 50 ans","50","38"))

# Exercice 78: re création de la méthode split()

#def split(phrase,caractere):
    #phrase_list=[]
    ## initialisation d'une variable temporaire
    #mot_tmp = ""
    ## si le caractère se trouve dans la phrase passé en paramètre 
    #if caractere in phrase:
        ## parcourir tous les indices des éléments de la phrase
        #for i in range(len(phrase)):
            #if phrase[i] != caractere:
                #mot_tmp += phrase[i]
                # si i est égale à l'index du dernier élément
                #if i == len(phrase)-1:
                    #phrase_list += [mot_tmp]
                    #return phrase_list
            #else:
                #phrase_list += [mot_tmp]
                #return phrase_list
            
#print(split("Bonjour Aurélie", " "))
#print(split("Salut, ça va ?",","))

# Exercice 79: recréation de la méthode isdigit()

#def isdigit(chaine):
    ## liste des chiffres
    #chiffres = ["0","1","2","3","4","5","6","7","8","9"]
    #for c in chaine:
        #if c not in chiffres:
            #return False
    #return True

#print(isdigit("123948493"))
#print(isdigit("edgte9be"))

# Exercice 80: les nombres palindromes

#def estUnPalindrome(nombre):
    #if nombre <= 10:
        #return False
    #else:
         #convertir en chaine de caractère
        #nombre_str = str(nombre)
        #nombre_str_inverse = nombre_str[::-1]
        #if nombre_str == nombre_str_inverse:
            #return True
        
#print(estUnPalindrome(10))
#print(estUnPalindrome(12521))

# Exercice 81: les nombres palindromes lié à l' exe 80

#nombre_palindrome = []
#for i in range(100,1000):
    #for j in range(100,1000):
        #nombre = i*j
        #if estUnPalindrome(nombre):
            #nombre_palindrome.append(nombre)

#plusGrand_palindrome = max(nombre_palindrome)
#print(plusGrand_palindrome)

# Exercice 82: Les nombre circulaires premiers
#import math

#def estPremier (nombre):
    # diviseur doit être supérieur ou égale à 2
    #diviseur = 2
    # tant que diviseur ne dépasse pas la racine carré de nombre
    #while diviseur <= math.sqrt(nombre):
        # si nombre est divisible par d alors
        #if nombre%diviseur == 0:
            ## si un diviseur est trouver alors nombre n'est pas premier
            #return False
        #diviseur += 1
    ## si on trouve aucun diviseur alors nombre est premier
    #return True

#def testCirculairePremier(nombre):
    # si le paramètre d'entré est nombre = 197 alors cette liste va contenir 197, 971 et 719
    #nombre_circulaire = []
    # convertir nombre en string
    #nombre = str(nombre)
    # trouver tous les nombre circulaire du paramètre d'entré nombre
    #for i in range (len(nombre)):
        #nombre_circulaire.append(nombre[i:] + nombre[i:])
        # tester si tous les nombres de la liste nombre_circulaire sont circulaire
        #premier_circulaire = True
        #for nombre in nombre_circulaire:
            # convertir nombre de string à entier
            #nombre = int(nombre)
            #utilisation de la fonction est premier
            #if not estPremier(nombre):
                # si un seul nombre n'est pas premier alors le nombre donné en parametre n'est pas circulaire premier
                #premier_circulaire = False
        #return premier_circulaire

#print(testCirculairePremier(9377))
#print(testCirculairePremier(36))

# Exercice 83: Nombre avec chiffre distincts

#def estDistinct(nombre):
    #nombre_str = str(nombre)
    #for chiffre in nombre_str:
        #if nombre_str.count(chiffre) >= 2:
            #return False
    #return True

#print(estDistinct(9647))
#print(estDistinct(1343))

# Exercice 84: 

#def codeSomme(nombre):
    #if nombre >= 100:
        #s = nombre
        #while s < 1 or s > 9:
            #nb = str(s)
            #s = 0
            #for lettre in nb:
                #s += int(lettre)
    #return str(s) + str(nombre)

#print(codeSomme(699810))
#print(codeSomme(3201))

# Exercice 85: recherche dichotomique

#def rechercheDicotomique(L,elt):
    # Trier la liste par ordre croissant
    #L.sort()
    #while L:
        ## index du milieu
        #index_milieu = len(L) // 2
        # si l'élément de l'index est égal à l'élément recherché
        #if elt == L[index_milieu]:
            #return True
        # si l'élément de l'index est plus petit que l'élément recherché
        #elif elt < L[index_milieu]:
            # garder que les éléments dont l'index est plus petit que l'index du milieu
            #L = L[:index_milieu]
        # Si l'élément recherché est plus grand que l'index_milieu
        #else: 
            # garder que les éléments dont l'index est plus grand que l'index milieu
            #L = L[index_milieu+1:]
    #return False

#print(rechercheDicotomique([6,9,15,36,41,43,47],41))
#print(rechercheDicotomique([-9,-1,3,4,7,11],0))

# Exercice 86: Triplet pythagoricien x,y,z

# 3 boucle for pour couvrir tousl les cas possibles de x,y,z

#for x in range(1,1000):
    #for y in range(x + 1,1000):
        #for z in range(y + 1,1000):
            # si les équations sont vérifiées
            #if x**2 + y**2 == z**2: 
                #if x+y+z == 1000:
                    # afficher les nombres x,y,z et le produit de ces nombres
                    #print("x = ", x)
                    #print("y = ", y)
                    #print("z = ", z)
                    #print("x*y*z = ", x*y*z)

# Exercice 87: traitement d'un fichier

#def traitementFichier(cheminFichier):
    ## ouverture en lecture du premier fichier
    #with open(cheminFichier, "r") as fichier1:
        # ouverture en écriture du 2 ème fichier
        #with open("test2.txt", "w") as fichier2:
            ## pour chaque ligne du fichier 1
            #for ligne in fichier1:
                ## supprimer les retours à la ligne pendant l'écriture dans le nouveau fichier
                #fichier2.write(ligne.rstrip("\n"))

#traitementFichier(r"C:\Users\Charles\Documents\exercices_python\test.txt")

# Exercice 88: Trie à bulle

#def triCroissant(L):
    # Parcourir tous les index de L
    #for i in range(len(L)):
        #pour les index de i
        #for j in range(i+1, len(L)):
            # si l'élément à l'index i est supérieur à l'élément se trouvant à j
            #if L[i] > L[j]:
                # échangé l'emplacement des 2 nombres
                #L[i], L[j] = L[j], L[i]
    #return L

#print(triCroissant([-3,5.3,2,7,1,2.3,9.5]))

# Exercice 89: Création d'une classe

## Définition d'une classe Personne

#class Personne : 
    ## constructeur init
    #def __init__ (self,taille,poids,age):
        ## attribut de la classe
        #self.taille = taille
        #self.poids = poids
        #self.age = age

    ## 1ère méthode de la classe
    #def calculIMC(self):
        ## formule de calcul IMC
        #return self.poids/(self.taille**2)
    ## 2ème méthode de la classe
    #def interpretationIMC(self):
        #Permet de faire un affichage selon le calcul IMC
        #if self.calculIMC() <= 18.5:
            #return "Insufisance pondérale"
        #elif self.calculIMC() >= 30:
            #return "Obèse"
        #return "surpoid ou normale"
    
#julien = Personne(1.80,114,34)

#print(julien.calculIMC())
#print(julien.interpretationIMC())

# Exercice 90: Classe rectangle

#class Rectangle:
    ## constructeur pour initialiser automatiquement l'instance qu'on va créer
    #def __init__(self,largeur,longueur):
        #self.longueur = longueur
        #self.largeur = largeur

    ## méthode qui permet de calculer le périmètre d'un rectangle
    #def Perimetre(self):
        #return 2*(self.largeur + self.longueur)
    
    ## méthode qui permet de calculer la surface d'un rectangle
    #def Surface(self):
        #return self.largeur * self.longueur
    
## ---- Création d'une instance + utilisation de méthodes ---  ##
## Création d'une instance de la classe rectangle
#a = int(input("Saisissez la largeur du rectangle : \n" ))
#b = int(input("Saisissez la longueur du rectangle : \n"))
#c = int(input("La hauteur du parallelepipede est de : \n"))

#rectangle1 = Rectangle(a,b)

#print ("\n La largeur du rectangle1 est ", rectangle1.largeur)
#print (" La longueur du rectangle1 est ", rectangle1.longueur)
#print (" La longueur du rectangle1 est ", c)
#print (" Le périmètre du rectangle1 est de ", rectangle1.Perimetre())
#print (" La surface du rectangle1 est de ", rectangle1.Surface())

# Exercice 91: Héritage d'une classe

#class Parallelepipede(Rectangle):
    ## constructeur
    #def __init__(self,largeur,longueur,hauteur):
        ## initialisation des attribut de la class parent
        #Rectangle.__init__(self,largeur,longueur)
        ## nouvel attribut de la class Parallelepipede
        #self.hauteur = hauteur
    ## métode qui calcule le volume
    #def Volume(self):
        #return self.longueur*self.largeur*self.hauteur
    
#Parallelepipede1 = Parallelepipede(a,b,c)

#print("Périmètre du parallelepipede : ", Parallelepipede1.Perimetre())
#print("Volume du parallelepipede : ", Parallelepipede1.Volume())

# Exercice 92: Classe compte banquaire

#class CompteBanquaire:
    ## constructeur d'initialisation des attributs
    #def __init__(self,nom = "maxime", solde = 600):
        #self.nom = nom
        #self.solde = solde
    
    ## méthode dépot
    #def depot(self,somme):
        #self.solde += somme
    ## méthode retrait
    #def retrait(self,somme):
        #self.solde -= somme
    ## méthode spéciale à revoir
    #def __repr__(self):
        #return "Le solde du compte banquaire de " + self.nom + " est de " + str(self.solde) + " euros"

# Exercice 93: Classe Voiture

#class Voiture:
    ## Construction d'initialisation des attributs ayant des attributs par défault
    #def __init__(self,marque="peugeot",couleur="noir",nomConducteur="aucun",kmDebut=16900):
        #self.marque = marque
        #self.couleur = couleur
        #self.nomConducteur = nomConducteur
        #self.kmDebut = kmDebut

    ## Méthode de changement de constructeur
    #def choixConducteur(self,nomConducteur):
        #self.nomConducteur = nomConducteur
        #return self.nomConducteur
    
    ## Méthode de calcule de la distance de circulation
    #def distanceCirculation(self,kmFin):
        #distance_parcourue = kmFin - self.kmDebut
        #return distance_parcourue
    
    #def afficherInfo(self):
        #kmActuel = self.distanceCirculation(20000) + self.kmDebut
        #return "La voiture " + self.marque + " de couleur " + self.couleur + " dont le conducteur est \n" + self.nomConducteur + " possède un kilométrage actuel de " + str(kmActuel) + " km."
    
#voiture1 = Voiture()

#print("Changement de conducteur : ",voiture1.choixConducteur("Patrick"))
#print("Distance de circulation : ", voiture1.distanceCirculation(39000))
#voiture1.afficherInfo()
    
# Exercice 94: Surcharge Opérateur

#class Point2D:
    ## constructeur d'initialisation des attributs
    #def __init__(self,x,y):
        #self.x=x
        #self.y=y
    ## surcharge de l'opérateur +
    #def __add__(self,p):
        #return self.x + p.x, self.y+p.y
    ## surcharge de l'opérateur -
    #def __sub__(self,p):
        #return self.x-p.x, self.y-p.y
    ## surcharge de l'opérateur *
    #def __mul__(self,p):
        #return self.x*p.x, self.y*p.y
    ## surcharge de l'opérateur /
    #def __truediv__(self,p):
        #return self.x/p.x, self.y/p.y
    
#p1 = Point2D(3,2)
#p2 = Point2D(1,4)
#print("p1-p2 = ", p1-p2)
#print("p1+p2 = ", p1+p2)
#print("p1*p2 = ", p1*p2)
#print("p1/p2 = ", p1/p2)

## Exercice 95: Surcharge d'opérateur

#class NombreComplexe:

    ## constructeur d'initialisation des attributs
    #def __init__(self,reel,img):
        #self.reel = reel
        #self.img = img

    ## surcharge de la représentation
    #def __str__(self):
        #return str(self.reel) + " + " + str(self.img) + "i"
    ## surcharge de la represantation
    #def __repr__(self):
        #return repr(self.reel) + " + " + repr(self.img) + "i"
    
#nbr1 = NombreComplexe(2,7)
#print(nbr1)

## Exercice 96: Classe liste personnalisé

#class ListePerso:
    #def __init__(self,*nombres):
        #self.nombres = []
        #for nombre in nombres:
            #if type(nombre) == int or type(nombre) == float:
                #self.nombres.append(nombre)
            #else:
                #print(f"Opération interdite : il n'est pas possible d'initialiser la liste avec {nombre}")
    ## méthode append
    #def append(self,nombre):
        ## si le nombre est un entier ou un décimal
        #if type(nombre) == int or type(nombre) == float:
            ## alors rajouter ce nombre à la liste
            #if nombre not in self.nombres:
                #self.nombres.append(nombre)
            #else:
                #return f"le nombre {nombre} existe déjà dans la liste {self}"
        #else: 
            #return f"Opération interdite : il n'est pas possible de rajouter le type {type(nombre)} dans la liste"
        
    
    #def __repr__(self):
        #return f"ListePerso({self.nombres})"

#L1 = ListePerso(5,2,3,7,9)
#print(L1)
#L1.append(2)
#L1.append("ABC")
#L1.append(10)
#print(L1)

# Exercice 97: Classe string personnalisé

#import string
## Listing de tous les chiffres de 0 à 9 + ajout des caractères "virgule" et "point"

#liste_caracteres = list(string.digits) + [",","."]
#class StrPerso:
    ## constructeur d'initialisation
    #def __init__(self,chaine):
        #liste_chaine = list(chaine)
        ## vérifier si dans "chaine", il existe un caractère interdit parmi la liste des caratères "liste_caracteres"
        #for c in liste_chaine:
            #if c in liste_caracteres:
                #print("L'instance créée ne doit contenir que des lettres alphabétiques:")
                #print(f"le caractère \"{c}\" sera supprimé")
                #chaine = chaine.replace(c, "")
        #self.chaine = chaine

    #def __add__(self, nouvelle_chaine):
        #if nouvelle_chaine in liste_caracteres:
            #return f"Vous ne pouvez pas ajouter de \"{nouvelle_chaine}\" à la chaine"
        #else:
            #self.chaine += nouvelle_chaine

        #return self.chaine
    
#chaine1 = StrPerso("Bon,jour")
#chaine1 + ","
#chaine1 + "."
#chaine2 = chaine1 + " ça va"
#chaine2

## Exercice 98: Ordonner un dictionnaire suivant la clé

#def ordonnerDict(d):
    ## Liste qui va contenir les tuples
    #liste_tuple = []
    ## liste des clé du dictionnaire
    #cle_d = list(d.keys())
    ## liste des valeurs
    #valeur_d = list(d.values())
    ## boucler sur (cle,valeur)
    #for cle,valeurs in zip(cle_d,valeur_d):
        ## ajouter le tuple dans la liste
        #liste_tuple.append((cle,valeurs))
        ## ordonner dans un ordre croissant suivant le premier élément du tuple
        #liste_tuple.sort(key = lambda x : x[0])
        ## retourner un dictionnaire
        #return dict(liste_tuple)
    
#print(ordonnerDict({8:9,2:3,9:11,7:33,11:48}))

## Exercice 99: La some maximale d'une sous liste
def SommeSeq(L,i,j):
    Lij = L[i:j+1]
    return sum(Lij)

def plusGrandSomme(L):
    ## initialisation var somme_max avec le premier élément de la liste L
    somme_max = L[0]
    ## parcourir les index de L
    for i in range(len(L)):
        ## parcourir les index de L en partant de i
        for j in range(i, len(L)):
            ## appel de fonction pour sommer la sequence de i à j 
            s = SommeSeq(L, i, j)
            ## si la somme trouver est supérieur à celle que nous avons initialisé
            if s > somme_max:
                ## enregistrer la sequence trouvé dans une variable
                seq = L[i:j+1]
                ## changer le contenu de somme_max avec le contenu de la nouvelle variable s
                somme_max = s

    return somme_max,seq

print(plusGrandSomme([-8,-4,6,8,-6,10,-4,-4]))
print(plusGrandSomme([-6,-1,8,-7,1,9,-1,2]))