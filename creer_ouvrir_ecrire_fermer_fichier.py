### Enregistrer le texte créé dans un fichier du disque dur

fichier = open('bonjour.txt','w') # créer et ouvrir un fichier intitulé 'bonjour'
                                  # paramètre 'w' spécifie que l'on va écrire ('write') du contenu dans ce fichier
fichier.write('Bonjour !')
fichier.close()
