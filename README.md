# lol_skin_count

Script comptant le nombre de champion pour lesquelles vous ne possédez pas de skins, et vous affiche cette liste.

## Utilisation

Le script ne fonctionne que lorsque le client est lancé, veillez donc à respecter cette condition.

Pour utiliser le script, il vous faut avoir Python d'installé, [Lien de téléchargement](https://www.python.org/downloads/) (pensez à redémarrer votre PC pour finaliser l'installation)

Je préconise si vous ne savez pas exécuter un script Python, de créer un fichier ```.bat``` sur votre bureau (où vous voulez en réalité).

### CREATION FICHIER .BAT

Créer un fichier texte normal et changer son extension (.txt → .bat). Dans ce fichier renseignez le code suivant :

```bat
[emplacement de votre executif python*] [emplacement global de lol_skin.py] 
cmd /k
```

L'emplaclement de votre exécutif python sera surement le suivant : ```C:/Users/[nom_user]/AppData/Local/Programs/Python/Python[version_python]/python.exe```, 
en remplaçant ```[nom_user]```et ```[version_python]```par ce qui vous correspond. Si vous avez spécfiez un autre dossier lors de l'installation, cet emplacement ne sera pas valide pour vous.

Pour obtenir l'emplacement global du script lol_skin.py, trouvez là où il s'est installé sur votre PC, allez dans ses propriétés (clic droit → Propriétés), allez dans l'onglet Sécurité et copiez la ligne "Nom de l'objet".
