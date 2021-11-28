### Ajouter du contenu à un fichier texte existant

# si nous lançons ce script plusieurs fois, nous verrons que plusieurs lignes
# contenant le message 'Vous allez bien ?' sont apparues


fichier = open('bonjour.txt','a')         # ouvrir un fichier pré-existant pour y ajouter du contenu avec le paramètre 'a' (append)
                                          # si nous avions ouvert ce fichier en mode écriture avec le paramètre 'w'
                                          # et si nous avions utilisé la méthode 'write',
                                          # le contenu précedent aurait été écrasé
fichier.write('\n' + 'Vous allez bien ?') 
fichier.close()
