### Lire depuis un fichier texte

fichier = open('bonjour.txt','r') # paramètre 'r' : fichier ouvert en mode lecture (read)
message = fichier.read()          # méthode 'read' des objets de type fichier
print(message)                    # afficher le contenu du fichier 'bonjour.txt'
fichier.close()                   
