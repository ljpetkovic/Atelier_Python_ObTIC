### Ajouter du contenu à un fichier texte existant

fichier = open('bonjour.txt','a')         # ouvrir un fichier pré-existant pour y ajouter du contenu avec le paramètre 'a' (append)
                                          # si nous avions ouvert ce fichier en mode écriture avec le paramètre 'w'
                                          # et si nous avions utilisé la méthode 'write',
                                          # le contenu précedent sera écrasé
fichier.write('\n' + 'Vous allez bien ?') 
fichier.close()
