# importation du document txt
import os
# le fichier existe
if os.path.exists("course.txt"):
    print("Le fichier existe !")
else:
    # le fichier n'existe pas je le crée
    print("Le fichier n'existe pas, je crée le fichier.")
    path = "C:\\Users\\Utilisateur\\PycharmProjects\\test"
    file = os.path.join(path,"course.txt")
    open(file,'a').close()


ok = input('souhaite tu faire les courses? (y/n)')

while ok == 'y':
    course = input('tu souhaite ajouter,supprimer,voir un produit? add/delete/see ')
    if course == 'add':
        add =input('quelle produit souhaite tu ajouter ?')
        fichier = open("course.txt", "a")
        print(f'\n tu as ajoute le produit suivant : {add}')
        fichier.write(f'\n{add}')
        fichier.close()

        ok = input('on continue les courses ? (y/n)')

    elif course == 'delete':
        supp=input("qu'elle produit souhaite tu modifier ?")
        fichier = open("course.txt", "r")
        new_fichier = [element.replace(supp,'') for element in fichier]


        fichier.close()
        fichier = open("course.txt", "w")
        fichier.write(' '.join(new_fichier))
        fichier.close()

        ok = input('on continue les courses ? (y/n)')

    else:
        fichier = open("course.txt","r")
        message = fichier.read()
        print(message)
        fichier.close()

        ok = input('on continue les courses ? (y/n)')



if ok == 'n':
    print('à bientôt')
else:
    print("je n'ai pas compris")