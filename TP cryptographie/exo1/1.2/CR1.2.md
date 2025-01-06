# Vérifier l'intrédrité d'un fichier téléchargé

### télécharger le fichier d'installation
[lien pour télécharger le fichier](http://google.com)

Téléchargez le fichier d'installation correspondant à la version pour architecture win64, version
française, version msi.
### ouvrir et copier un fichier
Ouvrez le fichier SHA256SUMS et copiez l'empreinte SHA256 correspondant à cette version dans un
fichier empreinte_officielle.txt

[empreinte_officielle](empreinte_officielle.txt)
### calculer
alculez l'empreinte du fichier msi téléchargé et enregistrez l'empreinte dans un fichier
empreinte_calculee.txt

[empreinte-calculee.txt](empreinte_calculee.txt)
```cmd
>openssl dgst -sha256 "Firefox Setup 134.0b9.msi"
```
### Vérifier
Vérifiez que le fichier d'installation n'a pas été corrompu en comparant les deux empreintes. Vous
pouvez utiliser la commande Windows CMD fc (File Compare):
```cmd
fc /B empreinte_calculee.txt empreinte_officielle.txt
```