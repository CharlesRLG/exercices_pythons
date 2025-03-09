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

def ajoutElementDict(cle,valeur,d):
    d[cle] = valeur
    return d

print(ajoutElementDict("baptiste",29,{"julien":14,"laurent":31}))
print(ajoutElementDict("poids", 65.3,{}))